from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from ariflow.provideres.postgres.hooks.postgres import PostgresHook
import json

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
            pass
    
    def write_in_db(self):
        self.postgres_hook.bulk_load(self.config.get('table_name'), '../tmp/file.tsv')