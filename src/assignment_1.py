from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Define Python functions for tasks
def task1():
    print("This is the first task that was created")

def task2():
    print("This is the second task for demo dag")

def task3():
    print("This is the third task for demo dag")

def task4():
    print("This is the fourth task for demo dag")

def task5():
    print("This is the fifth task for demo dag")

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 7),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
with DAG(
    'demo_dag_v01',
    default_args=default_args,
    description='A simple demo DAG',
    schedule_interval=timedelta(days=1),
) as dag:
    # Define tasks
    task_1 = PythonOperator(
        task_id='first_task',
        python_callable=task1,
    )
    task_2 = PythonOperator(
        task_id='second_task',
        python_callable=task2,
    )

    task_3 = PythonOperator(
        task_id='third_task',
        python_callable=task3,
    )

    task_4 = PythonOperator(
        task_id='fourth_task',
        python_callable=task4,
    )

    task_5 = PythonOperator(
        task_id='fifth_task',
        python_callable=task5,
    )

    # Define task dependencies
    task_1 >> task_2 >> task_3 >> [task_4, task_5]

