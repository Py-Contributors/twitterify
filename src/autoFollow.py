import time
import tweepy

from config import logging, create_api


def auto_follow(api):
    logging.info("Starting following Script")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logging.info(f"Following {follower.name}")
            follower.follow()


def main():
    api = create_api()
    while True:
        auto_follow(api)
        logging.info("Waiting...")
        time.sleep(60 * 60)


if __name__ == '__main__':
    main()
