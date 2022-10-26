import time
import tweepy

from config import logging, create_api


def auto_follow(api):
    logging.info("Starting following Script")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            follower.follow()
            followers_count = follower.followers_count
            print(f"Following {follower.name} with {followers_count} followers")
            time.sleep(60)


if __name__ == '__main__':
    api = create_api()
    auto_follow(api)
