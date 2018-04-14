import datetime
import os
import signal
import time

from coincheck.api import Api
from models import Ticker


access_key = os.getenv('COINCHECK_ACCESS_KEY', '')
secret_key = os.getenv('COINCHECK_SECRET_KEY', '')
api = Api(access_key, secret_key)


def task(arg1, arg2):
    r = api.ticker()
    t = datetime.datetime.fromtimestamp(int(r['timestamp']))
    print(r)
    if Ticker.select().where(Ticker.timestamp == t).count() == 0:
        Ticker.create(
            last=r['last'],
            bid=r['bid'],
            ask=r['ask'],
            high=r['high'],
            low=r['low'],
            volume=r['volume'],
            timestamp=t
        )


if __name__ == '__main__':
    signal.signal(signal.SIGALRM, task)
    signal.setitimer(signal.ITIMER_REAL, 5, 5)

    while True:
        time.sleep(30)

