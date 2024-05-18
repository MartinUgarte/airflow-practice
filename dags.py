from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'code2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5), 
}

with DAG (
    dag_id='our_first_dag_v4',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2021, 7, 29, 2), # everyday at 2am
    schedule_interval='@daily', 
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello world, this is the first task'
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo hello world, this is the second task and will be running after task1'
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo hello world, this is the third task and will be runnig after task1 and with the same time as task2'
    )

    # Task Dependencies Method 1
    #task1.set_downstream(task2)
    #task1.set_downstream(task3)

    # # Task Dependencies Method 2
    #task1 >> task2
    #task1 >> task3

    # Task Dependencies Method 3
    task1 >> [task2, task3]