# coding: utf-8

# Import libraries
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json
import sys

# Import twitter access keys
from credentials import *

WORDS = ['a', 'i', 'to', 'you', 'the', 'is', 'in']

class TweetsListener(StreamListener):
    """ A listener class that listens to the stream
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, csocket):
        super().__init__()
        self.client_socket = csocket
        
    def on_data(self, data):
        try:
            self.client_socket.sendall(data.encode('utf-8'))
            return True

        except BaseException as e:
            print("Error in Listener class: %s" % str(e))
            return False

    def on_error(self, status_code):
        print ("Error: ", status_code)
        return super().on_error(status_code)

def sendData(c_socket):
    """This function takes the socket object. 
    It creates an instance of class 'TweetsListener' and starts a stream.
    This twitter stream will search for given keywords

    Arguments:
        c_socket {socket connection} -- Local TCP Socket connection
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    
    # Instantiate 'TweetsListener' class
    stream_listener = TweetsListener(c_socket)
    # Create listener stream object
    twitter_stream = Stream(auth=auth, listener=stream_listener)
    
    # Twitter's filter.json API endpoint to search for keywords only
    twitter_stream.filter(languages=["en"], track=WORDS)

def socket_connect():
    """Creates a socket connection and send the connection to twitter stream class instance.
    """
    try:
        # local machine name
        TCP_IP = "localhost"
        # Reserve a port for your service                                       
        TCP_PORT = 9010 
        # Create a socket object                                           
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind to the port       
        s.bind((TCP_IP, TCP_PORT))                                  
        
        print("Listening on port: %s" % str(TCP_PORT))
        # Now wait for client connection.
        s.listen(5)
        # Establish connection with client.         
        conn, addr = s.accept()        
        
        print("Received request from: " + str(addr))
        sendData(conn)
    except BaseException as e:
        print("Error in Socket connection: %s" % str(e))



if __name__ == '__main__':
    socket_connect()
    #socket_connect(sys.argv[1])

'''
Create a socket object
AF_INET is the Internet address family for IPv4.
SOCK_STREAM is the socket type for TCP
# Using bind associate the socket with a specific network interface and port number
# listen() enables a server to accept() connections. It makes it a “listening” socket.
# Listen specifies the number of unaccepted connections that the system will 
# allow before refusing new connections
# accept() blocks and waits for an incoming connection. When a client connects, 
# it returns a new socket object representing the connection.
'''