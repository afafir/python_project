FROM python:3.8.16

ENV PYTHONBUFFERED 1

RUN mkdir /backend

WORKDIR /backend

COPY ../../backend /backend

RUN pip install -r requirements.txt
RUN python -m deeppavlov install squad_ru_bert
