from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'code2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

with DAG(

) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo This is a simple bash command!'
    )