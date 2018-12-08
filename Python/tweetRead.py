import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json

consumer_key = 'ectXmoPNpiFz2w4GRO6b2Gpwk'
consumer_secret = '8uuV81v1ErQUY646QCN7QVgkvfErhtaycYnar1CZHJ0bML6KjA'
access_token = '500698296-OYjSM2S6cEnEfYGyCy0cYNc11pP8bagPaOdHEhY7'
access_secret = 'v5xWObrBLv9DbiTPhWpXltFc1jgIbqi5vjhpONf74LvJn'

class TweetsListener(StreamListener):

    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, data):
        try:
            msg = json.loads( data )
            print( msg['text'].encode('utf-8') )
            self.client_socket.send( msg['text'].encode('utf-8') )
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    twitter_stream = Stream(auth, TweetsListener(c_socket))
    twitter_stream.filter(track=['kerela'])

if __name__ == "__main__":
    s = socket.socket()         # Create a socket object
    host = "127.0.0.1"          # Get local machine name
    port = 5555                 # Reserve a port for your service.

    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    s.bind((host, port))        # Bind to the port

    print("Listening on port: %s" % str(port))

    try:
        s.listen(5)                    # Now wait for client connection.
    except:
        print("Error")

    conn, adr = s.accept()         # Establish connection with client.
    print('connected with ' + adr[0] + ':' + str(adr[1]))
    while True:
        data = conn.recv(50)
        print(data)
        if not data:
            break
        conn.sendall(data)
    conn.close()
    s.close()

#     print( "Received request from: " + str( addr ) )

#     sendData( c )