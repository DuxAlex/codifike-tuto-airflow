from airflow import DAG
from datetime import datetime
from airflow.operator.python import PythonOperator, BranchPythonOperator
import pandas as pandas
import requests
import json

def captura_conta_dados():
    url = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"
    response = requests.get(url)
    df = pd.DataFrame(json.loads(response.content))
    qtd = len(df.index)
    return qtd
    
with DAG('tutorial_dag', start_date = datetime (2021,12,1),
        schedule_interval = ' 30 * * * *', catchup = false) as dag:

    captura_conta_dados = PythonOperator(
        task_id = 'captura_conta_dados',
        python_callable = captura_conta_dados, 
    )
