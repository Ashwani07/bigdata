# coding: utf-8

# Import libraries
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from kafka import SimpleProducer, KafkaClient

# Import twitter access keys
from credentials import *

WORDS = ['a', 'i', 'to', 'you', 'the', 'is', 'in']

class TweetsListener(StreamListener):
    """ A listener class that listens to the stream
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self):
        super().__init__()
        
    def on_data(self, data):
        try:
            producer.send_messages("twitter", data.encode('utf-8'))
            return True

        except BaseException as e:
            print("Error in Listener class: %s" % str(e))
            return False

    def on_error(self, status_code):
        print ("Error: ", status_code)
        return super().on_error(status_code)


try:
    kafka = KafkaClient("localhost:9092")
    producer = SimpleProducer(kafka)

except BaseException as e:
    print("Error in kafka: %s" % str(e))
else:
    # Authentication and access using keys:
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Instantiate 'TweetsListener' class
    stream_listener = TweetsListener()

    # Create listener stream object
    twitter_stream = Stream(auth=auth, listener=stream_listener)

    # Twitter's filter.json API endpoint to search for keywords only
    twitter_stream.filter(languages=["en"], track=WORDS)
