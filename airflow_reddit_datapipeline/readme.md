`docker compose up -d --build `
<br>
Error : failed to solve: image "docker.io/library/custom-airflow:2.7.1-python3.9": already exists
# To fix the error : 
`docker images` <br>
`docker rmi custom-airflow:2.7.1-python3.9`<br>
`docker build --no-cache -t custom-airflow:2.7.1-python3.9 .`<br>
`docker compose up -d --build`<br>