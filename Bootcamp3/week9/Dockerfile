# Deriving the python image
FROM python:3.8.3-slim

# Create a working directory in Docker, makes life easier when running instructions
WORKDIR /app

# Copies all the source code into our directory to the Docker image
COPY . /app

# Installs all the libraries we will need to execute the code
# if you want to use the requirements.txt file, use the first line of code
# RUN pip3 install -r requirements.txt
RUN pip3 install psycopg2-binary pandas boto3

# Tell Docker the command to run inside the container
CMD ["python3", "main.py"]
