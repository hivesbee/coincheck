import os
from coincheck.api import Api


if __name__ == '__main__':
    access_key = os.getenv('COINCHECK_ACCESS_KEY', '')
    secret_key = os.getenv('COINCHECK_SECRET_KEY', '')
    api = Api(access_key, secret_key)
    r = api.ticker()
    print(r)

