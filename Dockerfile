FROM python:3

RUN apt-get update
RUN apt-get -y install locales && \
    localdef -f UTF-8 -i ja_JP.UTF-8
RUN apt-get -y install vim less

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN mkdir -p /root/src
COPY requirement.txt /coor/src
WORKDIR /root/src

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirement.txt
