FROM python:3.6.5 

RUN pip install kafka --proxy="http://10.139.0.132:8080"

WORKDIR /app 
COPY producer.py .
COPY prod.py .  
RUN ["/bin/bash"]
