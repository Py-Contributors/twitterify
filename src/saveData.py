# Save number of tweets in csv format for a specific time periods 
# including id, name, twitter handle, location
# 
#

import tweepy
import pandas as pd

from config import create_api

api = create_api()

query = "#python"
date_since= "2019-01-01"
total_tweets = 100

filter_words = query + " -filter:retweets"

tweets = tweepy.Cursor(
    api.search,
    q=filter_words,
    lang='en',
    since=date_since).items(total_tweets)

tweet_data = [[
               tweet.user.id_str,
               tweet.user.screen_name,
               tweet.user.name,
               tweet.user.followers_count,
               tweet.user.location, 
               tweet.text,
               tweet.user.verified,
               tweet.user.created_at,
               tweet.user.statuses_count,
               ] for tweet in tweets]


tweet_data = pd.DataFrame(data=tweet_data,
                          columns=[
                          "id", 
                          "twitter_handle", 
                          "name", 
                          "total_followers", 
                          "location", 
                          "tweet", 
                          "is_verified",
                          "created_at",
                          "total_tweets",
                          ])

#print(tweet_data)
tweet_data.to_csv(f"{total_tweets}_{query}_{date_since}.csv")