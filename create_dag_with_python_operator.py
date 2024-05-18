from airflow import DAG 
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'code2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

def get_name(ti):
    # return 'Jerry' doesnt work if I want to distinguish more than one returning value
    ti.xcom_push(key='first_name', value='Jerry')
    ti.xcom_push(key='last_name', value='Garcia')

def get_age(ti):
    ti.xcom_push(key='age', value=25)

def greet(ti): # ti = task instance
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"Hello World! My name is {first_name} {last_name}, and I a {age} years old.")

with DAG (
    default_args=default_args,
    dag_id='our_dag_with_python_operator_v6',
    description='This is our first dag that we write with PythonOperator',
    start_date=datetime(2021, 7, 29, 2),
    schedule_interval='@daily',
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        #op_kwargs={'age': 25}
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    [task2, task3] >> task1