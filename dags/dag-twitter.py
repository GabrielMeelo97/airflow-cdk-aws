from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from dags.functions.dados_twitter import handler as h


dag = DAG('coleta_twitter', description='Coleta dados do twitter sobre determinado assunto', schedule_interval='@daily', start_date=datetime(2022, 3, 20), catchup=False)


twitter_operator = PythonOperator(task_id='twitter_task', python_callable=h.main, dag=dag)
