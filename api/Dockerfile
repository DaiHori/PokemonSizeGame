FROM python:3.8.5-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/pokemonsizegame/api

RUN apk update

ADD . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt