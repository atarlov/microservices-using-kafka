from __future__ import print_function  
from kafka import KafkaConsumer
import sys 
import argparse

KAFKA_TOPIC = 'demo'
KAFKA_BROKERS = 'kafka:9092' 

parser = argparse.ArgumentParser()
parser.add_argument('--topic', '-t',  dest='topic', help='set topic')
args = parser.parse_args()

KAFKA_TOPIC=args.topic

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BROKERS,
                         auto_offset_reset='earliest')

try:
    for m in consumer:
        print(m.value)
except KeyboardInterrupt:
    sys.exit()
