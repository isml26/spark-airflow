from datetime import datetime
from airflow import DAG

default_args = {
    'owner':'airscholar',
    'start_date': datetime(2024,1,8,19,0),
}

def stream_data():
    import json
    import requests

    res = requests.get('https://randomuser.me/api/')
    print(res.json())


# with DAG('user_authomation',default_args=default_args,schedule_interval='@daily',catchup=False) as dag:
#     streaming_task = PythonOperator(
#         task_id = 'stream_data_from_api',
#         python_callable=stream_data
#     )

stream_data()