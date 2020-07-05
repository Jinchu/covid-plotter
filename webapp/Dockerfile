FROM ubuntu:focal

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt -y upgrade
RUN apt -y install \
            python3-bs4 \
            python3-pip \
            wget
RUN update-ca-certificates

RUN pip3 install flask flask-WTF
RUN pip3 install -U matplotlib

RUN useradd -m tracker
USER tracker
RUN mkdir -p /home/tracker/webapp/
RUN mkdir -p /home/tracker/static/plots/
COPY . /home/tracker/webapp/
WORKDIR /home/tracker/webapp/

LABEL local.covid-web.release-date="Sun, 05 Jul 2020"
LABEL local.covid-web.version="20200705"

CMD ["python3", "covidtracker.py"]

EXPOSE 8000
