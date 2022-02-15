# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /home

# upgrade pip.
RUN python -m pip3 install --upgrade pip

# install all the packages.
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy project files to dir.
COPY  ../../ ./app/secretary-app/

# running the app
RUN python ./app/secretary-app/app.py
