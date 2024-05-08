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
    'start_date': datetime(2024, 5, 8),
}

# Instantiate the DAG object
dag = DAG(
    'scheduling_options_dag_v01',
    default_args=default_args,
    description='An example DAG demonstrating different scheduling options',
    schedule_interval=None,  # We'll define specific start times using cron expressions
)

# Define tasks
task1 = EmptyOperator(task_id='task1', dag=dag)
task2 = EmptyOperator(task_id='task2', dag=dag)

# Define Python functions for tasks
def task3_function():
    print("Task 3 executed at 6:00 AM")

def task4_function():
    print("Task 4 executed every Monday at 8:00 AM")

def task5_function():
    print("Task 5 executed every hour")

# Define PythonOperators for tasks 3, 4, and 5 with specific cron expressions
task3 = PythonOperator(
    task_id='task3',
    python_callable=task3_function,
    dag=dag,
    schedule_interval='0 6 * * *'  # Runs at 6:00 AM every day
)

task4 = PythonOperator(
    task_id='task4',
    python_callable=task4_function,
    dag=dag,
    schedule_interval='0 8 * * 1'  # Runs at 8:00 AM every Monday
)

task5 = PythonOperator(
    task_id='task5',
    python_callable=task5_function,
    dag=dag,
    schedule_interval='@hourly'  # Runs every hour
)

# Define dependencies
task1 >> [task3, task4, task5]  # Task 1 is upstream for all other tasks
task2 >> task3  # Task 2 is upstream for Task 3

