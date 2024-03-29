import tweepy

from config import create_api
from config import logging


class AutoRetweeter(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logging.info(f"Processing Tweet ID: {tweet.id}")
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            return

        if not tweet.retweeted:
            try:
                tweet.retweet()
                logging.info("Retweet Done.")
            except Exception:
                logging.error(f"Already Retweeted {tweet.id}", exc_info=False)
            try:
                tweet.user.follow()
                logging.info(f"Following {tweet.user.screen_name}")
            except Exception:
                logging.error(f"Already following {tweet.user.screen_name}")

    def on_error(self, status):
        logging.error(status)


def main(keywords: list):
    api = create_api()
    tweet_listener = AutoRetweeter(api)
    stream = tweepy.Stream(api.auth, tweet_listener)

    stream.filter(track=keywords, languages=['en'])


if __name__ == '__main__':
    keywords = ["<your keywords>", "<your keywords>"]
    main(keywords)
