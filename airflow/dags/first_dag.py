from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(dag_id="first_dag", start_date=datetime(2023, 11, 26), schedule=None) as dag:
    EmptyOperator(task_id="dummy_op")


if __name__ == "__main__":
    dag.test()
