FROM python:3.8.5-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/pokemonsizegame/api

ADD . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt