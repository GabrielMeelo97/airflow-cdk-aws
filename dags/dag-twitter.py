from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from dags.functions.dados_twitter.twitter\handler.py

def print_hello():
 return 'Hello Wolrd'

dag = DAG('hello_world_ondemand', description='Hello world example', schedule_interval=None, start_date=datetime(2017, 3, 20), catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries = 3, dag=dag)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

dummy_operator >> hello_operator
