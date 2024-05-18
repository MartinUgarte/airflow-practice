from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'code2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5), 
}

with DAG (
    dag_id='our_first_dag',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2021, 7, 29, 2), # everyday at 2am
    schedule_interval='@daily', 
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello world, this is the first task'
    )

    task1