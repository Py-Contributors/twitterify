import tweepy

from src.config import create_api
from src.autoRetweet import AutoRetweeter

def main(api):
    tweet_listener = AutoRetweeter(api)
    stream = tweepy.Stream(api.auth, tweet_listener)
    keywords = ["#Python", "#machinelearning", "#deeplearning", "#artificialintelligence"]
    stream.filter(track=keywords, languages=['en'])

if __name__ == '__main__':
    api = create_api()
    main(api)