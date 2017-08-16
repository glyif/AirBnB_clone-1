FROM ubuntu:14.04
MAINTAINER glyif <122@holbertonschool.com>

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    ca-certificates \
    gcc \
    git \
    libpq-dev \
    make \
    mercurial \
    pkg-config \
    python3.4 \
    python3.4-dev \
    ssh \
    && apt-get autoremove \
    && apt-get clean
ADD https://bootstrap.pypa.io/get-pip.py /root/get-pip.py
RUN python3.4 /root/get-pip.py

