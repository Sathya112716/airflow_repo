from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 5, 8),
    # 'end_date': datetime(2024, 12, 31),
}

# Instantiate the DAG object
dag = DAG(
    'dependency_dag_v01',
    default_args=default_args,
    description='An example DAG demonstrating task dependencies',
    schedule_interval=timedelta(days=1),
)

# Define a Python function to be executed by the PythonOperator
def print_hello():
    return 'Hello Airflow!'

# Define tasks
start_task = EmptyOperator(task_id='start_task', dag=dag)
task1 = EmptyOperator(task_id='task1', dag=dag)
task2 = EmptyOperator(task_id='task2', dag=dag)
task3 = PythonOperator(task_id='task3', python_callable=print_hello, dag=dag)
end_task = EmptyOperator(task_id='end_task', dag=dag)

# Define dependencies
start_task >> task1
start_task >> task2
task1 >> task3
task2 >> task3
task3 >> end_task

