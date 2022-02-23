# syntax=docker/dockerfile:1

FROM python:3.9-slim

WORKDIR /home

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# install all the packages.
COPY ./bin/docker/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy project files to dir.
ENV APP_HOME /app
ENV SEC_HOME /app/secretary-app

WORKDIR $APP_HOME
COPY  . secretary-app/

WORKDIR $SEC_HOME
# running the app
CMD [ "python", "./app.py" ]

