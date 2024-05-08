from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
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
    'trigger_dagrun_operator_dag_v01',
    default_args=default_args,
    description='A DAG describing the TriggerDagRunOperator',
    schedule_interval=timedelta(days=1),
) as dag:
    # Define tasks using TriggerDagRunOperator
    trigger_dag_1 = TriggerDagRunOperator(
        task_id='trigger_dag_1',
        trigger_dag_id='bash_operator_v03',  # ID of the DAG to trigger
    )

    trigger_dag_2 = TriggerDagRunOperator(
        task_id='trigger_dag_2',
        trigger_dag_id='python_operator_dag_v01',  # ID of the DAG to trigger
    )


    # Define task dependencies
    trigger_dag_1 >> trigger_dag_2

