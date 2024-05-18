from airflow import DAG 
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'code2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

def greet(name, age):
    print(f"Hello World! My name is {name}, and I a {age} years old.")

with DAG (
    default_args=default_args,
    dag_id='our_dag_with_python_operator_v01',
    description='This is our first dag that we write with PythonOperator',
    start_date=datetime(2021, 7, 29, 2),
    schedule_interval='@daily',
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
        op_kwargs={'name': 'John', 'age': 25}
    )

    task1