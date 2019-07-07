from kafka import KafkaConsumer

# continuous loop
loop = 1
while loop == 1:

    # initialize consumer to given topic and broker. IP is of kafka docker container.
    consumer = KafkaConsumer('test-topic', group_id='consumer-1', \
        bootstrap_servers='192.168.32.3:9094')

    # loop and print messages
    for msg in consumer:
        print (msg)
