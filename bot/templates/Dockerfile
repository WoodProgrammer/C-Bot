FROM python:latest
COPY requirements.txt .
COPY {{payload}} ./{{payload}}
RUN pip3 install -r requirements.txt
WORKDIR {{payload}}
ENTRYPOINT ['python3','{{payload_file}}']
