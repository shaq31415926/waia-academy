# Deriving the python image
FROM python:3.8-buster

# installs all the libraries we will need to execute the code
COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

# Create a working directory in Docker, makes life easier when running instructions
WORKDIR /app

# Copies all the source code into our directory to the Docker image
COPY . /app

# tell Docker the command to run inside the container
CMD ["python", "./main.py"]