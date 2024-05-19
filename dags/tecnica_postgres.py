from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta
from operators.PostgresFileOperator import PostgresFileOperator 
from airflow.operators.bash import BashOperator
import datetime

DATE = str(datetime.date.today()).replace('-', '')

default_args = {
    "owner": "martin",
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="tecnica_postgres",
    default_args=default_args,
    start_date=datetime(2023,2,17),
    schedule_interval='0 0 * * *'
) as dag:
    task_1 = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="postgres_localhost",
        sql="""
            create table if not exists tecnica_ml (
                id varchar(100),
                site_id varchar(100),
                title varchar(100),
                price varchar(100),
                sold_quantity varchar(100),
                thumbnail varchar(100),
                created_date varchar(8),
                primary key(id, created_date)
            )
        """
    ),
    task_2 = BashOperator(
        task_id="consulting_API",
        bash_command="python3 tmp/consult_api.py"
    ),
    task_3 = PostgresFileOperator(
        task_id = "insert_data",
        operation="write",
        config={
            "table_name": "tecnica_ml"
        }
    )
    task_4 = PostgresFileOperator(
        task_id = "read_data",
        operation="read",
        config={"query": f""" 
                SELECT * from tecnica_ml 
                WHERE sold_quantity != 'null' 
                AND created_date={DATE} AND cast(price as decimal) * cast(sold_quantity as int) > 7000000
                """}
    )
    task_1 >> task_2 >> task_3