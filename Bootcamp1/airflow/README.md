## Requirements
The minimum requirements:
- Docker for Mac: [Docker >= 20.10.2](https://docs.docker.com/docker-for-mac/install/)
- Docker for Windows: 
  - Installation: [Docker](https://docs.docker.com/desktop/install/windows-install/)
  - Manual installation steps for older WSL version: [Docker WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)

### Instructions on how to execute the code
Copy the ``.env.example`` file to `.env` and fill out the environment vars.

Make sure you are executing the code from the airflow folder and you have Docker Desktop running.


1. Build a docker image with puckel/docker-airflow image

```bash
  docker image build -t local-airflow .
```

2. Run airflow with env variables

```bash
  docker run --env-file .env -d -p 8080:8080 local-airflow webserver
```

3. Access Airflow webserver at http://localhost:8080 and trigger the dag. Please note the pipeline dag will not work without the correct environment variables.


4. You can now add/modify DAGs in the dags folder, but this version does not automatically sync and you will need to delete the container, re-build the image and run the webserver.
