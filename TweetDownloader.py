from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from urllib.request import urlopen
import tweepy
import TwitterCredentials as TC
import json
import re
import TextPocessing


auth = OAuthHandler(TC.consumer_key, TC.consumer_secret)
auth.set_access_token(TC.access_key, TC.access_secret)
api = tweepy.API(auth)
hash_tags = ["Cyber Security"]


class TwitterAPI:

    def InitiateStream(self):
        listener = StdOutListener()
        stream = Stream(auth, listener)
        stream.filter(track=hash_tags)
        print("/////////////////////////////////////\n")
        print("Stream Started...\n")
        print("/////////////////////////////////////\n")

    def Search(self):
        print("/////////////////////////////////////\n")
        print("Beginning to download the timeline...\n")
        print("/////////////////////////////////////\n")
        search_results = api.search(q=str(hash_tags), count=50, lang = "en", tweet_mode='extended')
        clean_search = set(TextPocessing.RefactorSearchResults(search_results))   #self.RefactorSearchResults(search_results)
        print("/////////////////////////////////////\n")
        print("downloading finished, beginning the stream...\n")
        print("/////////////////////////////////////\n")
        self.InitiateStream()


class StdOutListener(StreamListener):

    def on_status(self, status):
        clean_text = TextPocessing.RefactorSearchStream(status)
        return

    def on_error(self, status_code,):
        if status_code == 420:
            print("The limit was exeeded")
            return False




if(__name__ == "__main__"):
    print("Here we go \n")
    Twitter = TwitterAPI()
    Twitter.Search()

















