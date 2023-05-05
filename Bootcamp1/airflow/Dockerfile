# Information about the image we are using can be found here: https://github.com/puckel/docker-airflow
FROM puckel/docker-airflow

# Create a working directory in Docker, makes life easier when running instructions
WORKDIR /usr/local/airflow/

# install libraries that are not in the Docker image e.g. boto3
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# copy dags to the dags folder in the image
COPY dags/. dags/
# copy the python scripts to the dags folder in the image
COPY src dags/src/