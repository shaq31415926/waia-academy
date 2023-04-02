# Deriving the python image
FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update -qq && apt-get install -y \
  && apt-get -y install nano \
  dumb-init \
  python3-dev python3-pip build-essential \
  gcc \
  libgmp3-dev \
  libpq-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && pip3 install --upgrade pip \
  && pip3 --no-cache-dir install awscli --upgrade

# installs all the libraries needed
COPY requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

WORKDIR /app

COPY . /app

EXPOSE 8888

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

#CMD instruction should be used to run the software
CMD ["python", "./main.py"]