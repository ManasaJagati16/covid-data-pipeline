from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'manasa',
    'start_date': datetime(2025, 6, 1),
    'retries': 1
}

with DAG(
    dag_id='covid_data_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    description='ETL pipeline to extract COVID data, upload to S3 and load to Snowflake',
    tags=['covid', 'ETL', 's3', 'snowflake']
) as dag:

    extract_task = BashOperator(
        task_id='extract_covid_data',
        bash_command='python3 ~/covid_data_pipeline/scripts/extract_covid_data.py'
    )

    upload_to_s3_task = BashOperator(
        task_id='upload_to_s3',
        bash_command='python3 ~/covid_data_pipeline/scripts/upload_to_s3.py'
    )

    load_to_snowflake_task = BashOperator(
        task_id='load_to_snowflake',
        bash_command='python3 ~/covid_data_pipeline/scripts/load_to_snowflake.py'
    )

    extract_task >> upload_to_s3_task >> load_to_snowflake_task
