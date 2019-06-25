# Ref: https://blog.k2datascience.com/running-kafka-using-docker-332207aec73c
from kafka import KafkaConsumer

# continuous loop
var = 1
while var == 1:

    # initialize consumer to given topic and broker. IP is of kafka docker container.
    consumer = KafkaConsumer('test-topic', group_id='consumer-1', \
        bootstrap_servers='172.19.0.3:9094')

    # loop and print messages
    for msg in consumer:
        print (msg)