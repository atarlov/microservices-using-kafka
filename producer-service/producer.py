from kafka import KafkaProducer

KAFKA_TOPIC= 'demo'
KAFKA_BROKERS = 'kafka:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKERS) 

if type(KAFKA_TOPIC) == bytes: 
    KAFKA_TOPIC=KAFKA_TOPIC.decode('utf-8')

messages = [b'one', b'two', b'three']
for m in messages: 
 producer.send(KAFKA_TOPIC, m)

producer.flush()
