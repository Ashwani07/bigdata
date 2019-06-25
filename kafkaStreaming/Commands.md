## Creating zookeeper container
docker run -d --name zookeeper -p 2181:2181 wurstmeister/zookeeper

## Creating kafka container
docker run -d --name kafka -p 7203:7203
            -p 9092:9092
            -e KAFKA_ADVERTISED_HOST_NAME=localhost
            -e ZOOKEEPER_IP=localhost wurstmeister/kafka

## Get inside the running container
docker exec -it zookeeper bash

## Create topic
docker run --rm wurstmeister/kafka kafka-topics.sh --create --topic senz --replication-factor 1 --partitions 1 --zookeeper 172.17.0.1:2181
