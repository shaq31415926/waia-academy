Build a docker image with puckel/docker-airflow image

```bash
  docker image build -t airflow .
```

Run airflow with env variables

```bash
  docker run --env-file .env -d -p 8080:8080 airflow webserver
```


