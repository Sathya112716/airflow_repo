from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Define Python functions for tasks
def print_hello():
    print("Hello, Airflow!")

def calculate_square():
    result = 5 * 5
    print("Square of 5:", result)

# Define default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 7),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
with DAG(
    'python_operator_dag_v01',
    default_args=default_args,
    description='A DAG describing the PythonOperator',
    schedule_interval=timedelta(days=1),
) as dag:
    # Define tasks using PythonOperator
    task_1 = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello,

    )
    task_2 = PythonOperator(
        task_id='calculate_square',
        python_callable=calculate_square,
    )
    # Define task dependencies
    task_1 >> task_2

