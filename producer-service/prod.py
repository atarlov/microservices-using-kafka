from kafka import KafkaProducer
import argparse 

#KAFKA_TOPIC= 'demo'
KAFKA_BROKERS = 'kafka:9092'
parser = argparse.ArgumentParser()
parser.add_argument('--topic', '-t',  dest='topic', help='set topic')
parser.add_argument('--message', '-m', dest='message', help='set message')
parser.add_argument('--port', '-p', dest='port', help='port')
args = parser.parse_args()

KAFKA_BROKERS='kafka:{}'.format(args.port)
KAFKA_TOPIC = args.topic

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKERS) 

if type(KAFKA_TOPIC) == bytes: 
    KAFKA_TOPIC=KAFKA_TOPIC.decode('utf-8')

producer.send(KAFKA_TOPIC, str.encode(args.message))
producer.flush()
