# microservices-using-kafka

# Create a topic 
/opt/kafka/bin/kafka-topics.sh --zookeeper zookeeper:2181 --create --topic helloKafka --partitions 1 --replication-factor 1 

>Created topic "helloKafka".

# Publish msg "Hello World" to a topic 
echo "Hello, World" | /opt/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic helloKafka > /dev/null.

# Consume the msg 
/opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic helloKafka --from-beginning 


# Describe a topic 
/opt/kafka/bin/kafka-topics.sh --describe --topic helloKafka --zookeeper zookeeper

### 
Topic:helloKafka        PartitionCount:1        ReplicationFactor:1     Configs:
Topic: helloKafka       Partition: 0    Leader: 1       Replicas: 1     Isr: 1

Zookeeper 
# Check with Zookeeper 
docker exec -it [zk_container_id] ./bin/zkCli.sh ls /brokers/topics

# Scale kafka 
docker-compose scale kafka=3

# Consumer 
docker exec -it `docker ps -aqf "name=microservicesusingkafka_consumer"` python consumer.py -t demo

# Producer 
docker exec -it `docker ps -aqf "name=microservicesusingkafka_producer"` python prod.py -p 9092 -t demo -m something

# Zookeeper - topics
docker exec -it `docker ps -aqf "name=microservicesusingkafka_zookeeper` ./bin/zkCli.sh ls /brokers/topics
