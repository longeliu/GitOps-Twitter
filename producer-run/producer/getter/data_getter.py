# data_reader.py
import pandas as pd
import json
import tweepy
import os

API_PATH = os.getcwd() + "/API_KEY.json"

class Info_Getter:
    def __init__(self, keyword):
        file = open(API_PATH)
        self.api_keys = json.load(file)
        self.keyword = keyword
        self.cursor()

    def cursor(self):
        auth = tweepy.OAuthHandler(self.api_keys["API_KEY"], self.api_keys["API_KEY_SECRET"])
        auth.set_access_token(self.api_keys["ACCESS_TOKEN"], self.api_keys["ACCESS_TOKEN_SECRET"])
        api = tweepy.API(auth)
        # Search for tweets containing a specific hashtag
        self.tweets = tweepy.Cursor(api.search_tweets, q = self.keyword).items()

if __name__ == '__main__':
    pass