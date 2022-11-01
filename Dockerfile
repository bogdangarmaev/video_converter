FROM python:3.10.8-bullseye

LABEL maintainer="bogdan <bogdangarmaev@gmail.com>"

USER root

WORKDIR /app
ADD . /app/
RUN apt-get update && apt-get install -y ffmpeg

RUN pip install wheel \
    && pip install -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*
