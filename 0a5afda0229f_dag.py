from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator, DatabricksRunNowOperator
from datetime import datetime, timedelta 

# Current date
#today = datetime.today()

# Define params for Submit Run Operator
notebook_task = {
    'notebook_path': '/Users/muhammaddurba@gmail.com/Spark data cleaning',
}

# Define params for Run Now Operator
notebook_params = {
    "Variable": 5
}

default_args = {
    'owner': '0a5afda0229f',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,  # set to 3 retries
    'retry_delay': timedelta(minutes=2)
}

with DAG('0a5afda0229f_dag',
         start_date=22-10-2023,  # setting start date as today
         schedule_interval='@daily',  # setting it to run daily
         catchup=False,
         default_args=default_args
         ) as dag:

    opr_submit_run = DatabricksSubmitRunOperator(
        task_id='submit_run',
        databricks_conn_id='databricks_default',
        existing_cluster_id='Pinterest Cluster',
        notebook_task=notebook_task
    )
    opr_submit_run
