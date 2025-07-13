`docker compose up -d --build `
<br>
Error : failed to solve: image "docker.io/library/custom-airflow:2.7.1-python3.9": already exists
# To fix the error : 
`docker images` <br>
`docker rmi custom-airflow:2.7.1-python3.9`<br>
`docker build --no-cache -t custom-airflow:2.7.1-python3.9 .`<br>
`docker compose up -d --build`<br>

To understand more about docker and the entire setup, [click here](https://chatgpt.com/share/67b771c9-6d90-8008-90eb-543946ba87ad)

## Architecture
![RedditDataEngineering.png](assets/RedditDataEngineering.png)
1. **Reddit API**: Source of the data.
2. **Apache Airflow & Celery**: Orchestrates the ETL process and manages task distribution.
3. **PostgreSQL**: Temporary storage and metadata management.
4. **Amazon S3**: Raw data storage.
5. **AWS Glue**: Data cataloging and ETL jobs.
6. **Amazon Athena**: SQL-based data transformation.
7. **Amazon Redshift**: Data warehousing and analytics.

# Code Flow : 

1. `/dags/reddit_dags.py` -> setup and #1. Extraction for reddit #2. Upload to S3 (later part)
2. from pipelines.reddit_pipeline import reddit_pipeline to the `/dags/reddit_dags.py` from `/pipelines/reddit_pipelines.py`
3. from etls.reddit_etl import connect_reddit to the `/pipelines/reddit_pipelines` from `/etls/reddit_etls.py`
4. We have a function in reddit_pipeline.py named as connect reddit, extract post which we are importing from reddit_etl.py
5. 
6. 
7. 
8. 


# Commands 
1. Activating venv `.\.venv\Scripts\Activate.ps1`
2. if you install any new dependencies do `pip freeze > requirements.txt` and rebuilt the docker using `docker compose up -d --build`
3. Rebuild/start all	`docker compose up -d`	Builds (if needed) and starts containers