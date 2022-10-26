# Save number of tweets in csv format for a specific time periods
# including id, name, twitter handle, location
#
#

import tweepy
import pandas as pd
import argparse

from config import create_api

arg = argparse.ArgumentParser()
arg.add_argument("-n", "--num_of_tweets", default=100,
                 help="number of tweets to be extracted")
arg.add_argument('-q', '--query', required=True,
                 help="query to save tweet about it(hastag)")
arg.add_argument('-d', '--date_since', help="data since the tweet wants")
args = arg.parse_args()

api = create_api()

query = args['query']
date_since = args['date_since']
total_tweets = args['num_of_tweets']
filter_words = query + " -filter:retweets"


def save_data():
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

    # print(tweet_data)
    tweet_data.to_csv(f"{total_tweets}_{query}_{date_since}.csv")


if __name__ == "__main__":
    save_data()
