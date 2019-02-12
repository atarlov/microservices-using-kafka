FROM python:3.6.5 
MAINTAINER assen.tarlov@gmail.com 

RUN pip install kafka --proxy="http://10.139.0.132:8080"

WORKDIR /app 
COPY consumer.py . 
RUN ["/bin/bash"]
