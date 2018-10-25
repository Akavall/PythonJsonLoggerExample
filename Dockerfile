FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y python python-dev python-distribute python-pip

RUN pip install python-json-logger

COPY PythonJsonLoggerExample PythonJsonLoggerExample

WORKDIR PythonJsonLoggerExample

CMD python my_file.py
