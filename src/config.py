import os
import tweepy
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(filename='app.log', 
                    format='%(levelname)s: %(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', 
                    level=logging.INFO)

logging.info("\n\n\nNewLog Starting...")

def create_api():
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
        print("Authentication OK")
    except Exception as e:
        logging.error("Error creating API", exc_info=True)
        raise e
    logging.info("API Created")
    return api
