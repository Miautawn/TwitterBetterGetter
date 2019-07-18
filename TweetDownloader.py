from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import TwitterCredentials as TC


class StdOutListener(StreamListener):
    def on_data(self, raw_data):
        print(raw_data)
        return

    def on_error(self, status_code,):
        print("This is an error")


if(__name__ == "__main__"):
    print("Here we go \n")
    print("this is consumer key: {}\n".format(TC.consumer_key))
    print("this is consumer secret: {}\n".format(TC.consumer_secret))
    print("this is access key: {}\n".format(TC.access_key))
    print("this is access secret: {}\n".format(TC.access_secret))
    listener = StdOutListener()
    auth = OAuthHandler(TC.consumer_key, TC.consumer_secret)
    auth.set_access_token(TC.access_key, TC.access_secret)
    stream = Stream(auth, listener)
    stream.filter(track=["Cyber Security"])









