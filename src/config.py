import os
import tweepy
import logging
from dotenv import load_dotenv


logging.basicConfig(format="%(levelname)s - %(asctime)s - %(name)s - %(message)s",
                    encoding="utf-8",
                    datefmt='%d/%m/%Y %I:%M:%S %p',
                    handlers=[
                        logging.FileHandler(os.path.join('dev.log')),
                        logging.StreamHandler()])

logging.info("Starting logging...")


def create_api():
    load_dotenv()
    API_KEY = os.environ['API_KEY']
    API_SECRET_KEY = os.environ['API_SECRET_KEY']
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth,
                     wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
        logging.info("Authentication OK")
    except Exception:
        raise Exception("Error during authentication, check your credentials")
    logging.info("API Created")
    return api
