from lxml import html
import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from io import BytesIO
from zipfile import ZipFile
import requests
import pandas as pd

from django.conf import settings
import redis

redis_instance = redis.StrictRedis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=1, decode_responses=True
)

IST = pytz.timezone("Asia/Kolkata")

# To emulate as browser, since API forbids Python requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"
}

BASE_URL = "https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx"

def _get_file_url(url: str) -> str:
    resp = requests.get(url, headers=headers).content
    root = html.fromstring(resp)

    # Finds the most recently updated link
    for el in root.xpath('//*[@id="ContentPlaceHolder1_btnhylZip"]'):
        try:
            return el.attrib['href']
        except:
            raise Exception("File link not available")


def get_dataframe(fileurl: str) -> pd.DataFrame:
    resp = requests.get(fileurl, headers=headers).content
    with ZipFile(BytesIO(resp)) as zipfile:
        for filename in zipfile.namelist():
            with zipfile.open(filename) as f:
                df = pd.read_csv(
                    f, usecols=["SC_CODE", "SC_NAME", "OPEN", "HIGH", "LOW", "CLOSE"]
                )
                return df


def set_to_redis(key, value):
    for k, v in value.items():
        redis_instance.hset(key, k, v)


def import_data_to_redis():
    url = _get_file_url(BASE_URL)
    print("Retrieving file from %s" % url)
    df = get_dataframe(url)

    # Flush database with previous data
    redis_instance.flushdb()

    for _, row in df.iterrows():
        values = row.to_dict()
        key = row["SC_NAME"]
        set_to_redis(key, values)

    print("Imported data to Redis")


def start():
    print("Job Logged")
    scheduler = BackgroundScheduler(timezone=IST)
    scheduler.add_job(import_data_to_redis, "cron", hour=19, minute=39)
    scheduler.start()
