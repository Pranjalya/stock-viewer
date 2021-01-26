from datetime import time, datetime
import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from io import BytesIO
from zipfile import ZipFile
import requests
import pandas as pd


BASE_URL = "https://www.bseindia.com/download/BhavCopy/Equity/"
IST = pytz.timezone('Asia/Kolkata')

# To emulate as browser, since API forbids Python requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

def _get_file_url(url: str) -> str:
    _filedate = datetime.now(IST).strftime("%d%m%y")
    return BASE_URL + 'EQ{}.ZIP'.format(_filedate)


def _get_dataframe(fileurl: str) -> pd.DataFrame:
    resp = requests.get(fileurl, headers=headers).content
    with ZipFile(BytesIO(resp)) as zipfile:
        for filename in zipfile.namelist():
            with zipfile.open(filename) as f:
                df = pd.read_csv(f, usecols=['SC_CODE', 'SC_NAME', 'OPEN', 'HIGH', 'LOW', 'CLOSE'])
                return df


def import_data():
    BASE_URL = "https://www.bseindia.com/download/BhavCopy/Equity/"
    df = _get_dataframe(_get_file_url(BASE_URL))




def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(import_data, trigger=time(1, 13))
    scheduler.start()
