FROM python:3.7-alpine
MAINTAINER Grupo Centro Mediaciona

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /Centro
WORKDIR /app
COPY ./app /app

RUN adduser -D usergit branch
USER user
