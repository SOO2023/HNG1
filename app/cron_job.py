import requests
import random
import logging
import os
from dotenv import load_dotenv

load_dotenv()
HOST_URL = os.getenv("HOST_URL")


logger = logging.getLogger("Cron-Job")
logging.basicConfig(
    level=logging.INFO,
    format="{asctime} - {name} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)


def keep_alive():
    number = random.randint(1, 1000)
    my_url = f"{HOST_URL}/api/classify-number?number={number}"
    try:
        res = requests.get(my_url).json()
        logger.info(msg=f"result: {res}")
    except Exception as err:
        logger.error(f"Oops! an error occurred: {err}")
