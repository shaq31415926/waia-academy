from datetime import datetime

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

from src.extract_transform_load import extract_transform_load


dag = DAG("etl-pipeline",
          description="Extracts Transforms and Loads Data",
          schedule_interval="@daily",
          start_date=datetime(2023,1,1),
          catchup=False)

start_dag = DummyOperator(task_id="start_dag", dag=dag)
end_dag = DummyOperator(task_id="end_dag", dag=dag)

etl_operator = PythonOperator(task_id="extract_transform_load_data",
                                  python_callable=extract_transform_load,
                                  dag=dag)

start_dag >> etl_operator >> end_dag