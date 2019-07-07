import time
import random
import string
from kafka import KafkaProducer

letters = string.ascii_lowercase

# create producer. IP is of kafka docker container.
producer = KafkaProducer(bootstrap_servers='192.168.32.3:9094')

# continuous loop
loop = 1
while loop == 1:

    # generate a random number and word
    num = random.randint(0, 10)
    word = ''.join(random.choice(letters) for i in range(num))

    # message value and key must be raw bytes
    num_bytes = bytes(str(num), encoding='utf-8')
    word_bytes = bytes(word, encoding='utf-8' )

    # send to topic on broker
    producer.send('test-topic', value=word_bytes, key=num_bytes)

    # wait 1 second
    time.sleep(1)