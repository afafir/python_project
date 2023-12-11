FROM python:3.8.16

ENV PYTHONBUFFERED 1

RUN mkdir /vk

WORKDIR /vk

COPY ../../vk /vk

RUN pip install -r requirements.txt
