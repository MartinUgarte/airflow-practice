from datatime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
    'owner': 'code2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

@dag(dag_id='dag_with_taskflow_api_v01',
    default_args=default_args,
    start_date=datetime(2021, 7, 29, 2),
    schedule_interval='@daily')
def hello_world_etl():
    #Each task is represented by a python funciton with the task decorator above

    @task(multiple_outputs=True)
    def get_name():
        return {
            'firstname': 'Jerry',
            'lastname': 'Garcia'
        }
    
    @task()
    def get_age():
        return 19  # Pushed to XComs
    
    @task()
    def greet(firstname, lastname, age):
        print(f'"Hello World! My name is {firstname} {lastname} and I am {age} years old!')

    # Dependency method
    name_dict = get_name()
    age = get_age()
    greet(firstname=name_dict['firstname'], lastname=name_dict['lastname'], age=age)

greet_dag = hello_world_etl()