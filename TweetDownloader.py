from tweepy.streaming import StreamListener
import datetime
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import TwitterCredentials as TC
import json


auth = OAuthHandler(TC.consumer_key, TC.consumer_secret)
auth.set_access_token(TC.access_key, TC.access_secret)
api = tweepy.API(auth)
hash_tags = ["Cyber Security"]


class TwitterAPI:

    def InitiateStream(self):
        listener = StdOutListener()
        stream = Stream(auth, listener)
        stream.filter(track=hash_tags)
        print("Stream Started")

    def Search(self):
        search_results = api.search(q=str(hash_tags), count=50, lang = "en", tweet_mode='extended')
        clean_search = self.RefactorSearchResults(search_results)


    def RefactorSearchResults(self, search):
        clean_results = []
        f = open("TimeStamp.txt", "r")
        for tweet in search:
            if "retweeted_status" in tweet._json:
                clean_results.append(tweet._json["retweeted_status"]["full_text"])
            else:
                clean_results.append(tweet._json["full_text"])

        f.close()
        f = open("TimeStamp.txt", "w").write(str(search[0].created_at))
        return clean_results








class StdOutListener(StreamListener):
    def on_data(self, raw_data):
        print(raw_data)

        return
    def on_error(self, status_code,):
        if status_code == 420:
            print("The limit was exeeded")
            return False




if(__name__ == "__main__"):
    print("Here we go \n")
    Twitter = TwitterAPI()
    Twitter.Search()

















