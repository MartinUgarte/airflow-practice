import os
from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from ariflow.provideres.postgres.hooks.postgres import PostgresHook
import json
import smtplib
import ssl
from email.message import EmailMessage
from airflow.models import Variable

class PostgresFileOperator(BaseOperator):

    @apply_defaults
    def __init__(self,
                 operation,
                 config={},
                 *args,
                 **kwargs):
        super(PostgresFileOperator, self).__init__(*args, **kwargs)
        self.operation = operation
        self.config = config
        self.postgres_hook = PostgresHook(postgres_conn_id='postgres_localhost')
    
    def execute(self, context):
        if self.operation == 'write':
            #escribir en la db
            self.write_in_db()
        elif self.operation == 'read':
            #leer la db
            self.read_from_db()
    
    def write_in_db(self):
        self.postgres_hook.bulk_load(self.config.get('table_name'), '../tmp/file.tsv')

    def read_from_db(self):
        # read from db with a SQL query
        conn = self.postgres_hook.get_conn()
        cursor = conn.cursor()
        cursor.execute(self.config.get('query'))

        data = [doc for doc in cursor]
        if data: # si hay resultados de mi query
            send_email(data)

def send_email(data):
    email_from = "mugarte@fi.uba.ar"
    passw = Variable.get('PASSW_EMAIL')
    email_to = "mugarte@fi.uba.ar"
    title = "ALERTA ! Items con demasiadas ventas"
    body = """
    Hemos detectado nuevos items con demasiadas ventas: {}
    """.format(data)
    email = EmailMessage()
    email['From'] = email_from
    email['To'] = email_to
    email['Subject'] = title
    email.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_from, passw)
        smtp.sendmail(email_from, email_to, email.as_string())