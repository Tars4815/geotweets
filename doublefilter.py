from __future__ import absolute_import, print_function

from tweepy import OAuthHandler, Stream, StreamListener

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after. Insert them here:
consumer_key="xxxxxxx"
consumer_secret="xxxxxxx"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section. Insert them here:
access_token="xxxxxxx"
access_token_secret="xxxxxxx"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_data(self, data):
        if 'basket' in data: #Keeping tweets only if they contains the word "basket" in their data
            print(data)
            with open('Prova1208.json', 'a') as tf: #Saving retrieved tweets in a .json file
                tf.write(data)
            return True
        
    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(locations=[-141.1,23.0,-67.1,53.5]) #Defining a bounding box where to search tweets
