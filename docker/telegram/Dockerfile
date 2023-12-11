FROM python:3.8.16

ENV PYTHONBUFFERED 1

RUN mkdir /telegram

WORKDIR /telegram

COPY ../../telegram /telegram

RUN pip install -r requirements.txt