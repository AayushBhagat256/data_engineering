from airflow import DAG
from datetime import datetime
import os
import sys

from airflow.operators.python import PythonOperator

sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
"""
We need to modify the path the above line does that,
The above line modifies the sys.path list, which is used by Python to determine where to look for modules and packages
when you use the import statement
Before: ['C:\\Users\\Aayush Bhagat\\Desktop\\data_engineering\\airflow_reddit_datapipeline\\dags',..,..]
After:  ['C:\\Users\\Aayush Bhagat\\Desktop\\data_engineering\\airflow_reddit_datapipeline',..,..]
"""

from pipelines.reddit_pipeline import reddit_pipeline


default_args = {
    'owner':'Aayush Bhagat',
    'start_date':datetime(2025,7,13),
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id = 'etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    # start_date=,
    tags=['reddit','etl','pipeline']
)

#1. Extraction for reddit
extract = PythonOperator(
    task_id = 'reddit_extraction',
    python_callable = reddit_pipeline,
    op_kwargs = {
        'filename' : f'reddit_{file_postfix}',
        'subreddit' : 'dataengineering', #A subreddit is a community on Reddit that focuses on a specific topic or interest
        'time_filter' : 'day',
        'limit' : 100 
        # we are going to fetch 100 subreddit or 100 posts for a particular day
        # the function reddit_pipeline is called from pipeline directory
    },
    dag = dag
)
#2. Upload to S3

# upload_s3 = PythonOperator(
#     task_id = 's3Upload',
#     python_callable= upload_s3_pipeline,
#     dag = dag
# )

# extract 
