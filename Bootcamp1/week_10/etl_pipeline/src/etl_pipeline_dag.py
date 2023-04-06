import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator
from extract import extract_transactional_data

DEFAULT_ARGS = {
    "owner": "shaq",
    "depends_on_past": False,
    "start_date": datetime.datetime(2022, 5, 19, 0, 0),
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    dag_id="etl-pipeline",
    default_args=DEFAULT_ARGS,
    schedule_interval=None,
    tags=["tesr"],
)

start_dag = DummyOperator(task_id="start_dag", dag=dag)
end_dag = DummyOperator(task_id="end_dag", dag=dag)

extract_job = PythonOperator(
    task_id="extract_transactional_data_job",
    python_callable=extract_transactional_data,
    dag=dag
)

start_dag >> extract_job >> end_dag
