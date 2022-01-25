from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'airflaw_test',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='this_is_first_dag_add_second_task',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2022,1,11,2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo Hello, this is my first dag. Are you OK?"
    )
    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo I am second task and will be running after first task"
    )
    task1.set_downstream(task2)
