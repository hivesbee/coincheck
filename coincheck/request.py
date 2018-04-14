import hashlib
import hmac
import json
import requests
import time


def fetch_public(url, params={}):
    p = build_params(params)
    u = ''.join([url, p])
    r = requests.get(u)

    return json.loads(r.text)


def fetch_private(url, params={}, access_key=None, secret_key=None):
    h = build_header(url, params, access_key, secret_key)
    r = requests.get(url, headers=h)

    return json.loads(r.text)


def create_private(url, params={}, access_key=None, secret_key=None):
    h = build_header(url, params, access_key, secret_key)
    r = requests.post(url, headers=h)

    return json.loads(r.text)


def delete_private(url, params={}, access_key=None, secret_key=None):
    h = build_header(url, params, access_key, secret_key)
    r = requests.delete(url, headers=h)

    return json.loads(r.text)


# util functions
def build_header(url, params={}, access_key=None, secret_key=None):
    n = nonce()
    p = build_params(params)
    m = ''.join([n, url, p])
    s = hmac.new(secret_key.encode(), m.encode(), hashlib.sha256).hexdigest()

    return {
        'ACCESS-KEY': access_key,
        'ACCESS-NONCE': n,
        'ACCESS-SIGNATURE': s
    }


def nonce():
    return str(int(time.time() * 1000000000))


def build_params(params={}):
    return '' if params == {} else '?{}'.format('&'.join(['='.join([k, str(v)]) for (k, v) in params.items()]))
