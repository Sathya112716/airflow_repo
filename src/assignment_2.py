from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Define default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 7),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
with DAG(
    'bash_operator_v03',
    default_args=default_args,
    description='A DAG describing the BashOperator',
    schedule_interval=timedelta(days=1),
) as dag:
    # Define tasks using BashOperator
    task_1 = BashOperator(
        task_id='print_hello',
        bash_command='echo "Hello, Airflow!"',
    )

    task_2 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    task_3 = BashOperator(
        task_id='print_message',
        bash_command='echo "This is a custom message"',
    )

    task_4 = BashOperator(
        task_id='calculate_square',
        bash_command='expr 5 \* 5',  # Calculate the square of 5
    )

    # Define task dependencies
    task_1 >> [task_2, task_3, task_4]

