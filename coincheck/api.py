import os
from coincheck import urls
from coincheck.request import fetch_public, fetch_private, create_private, delete_private, build_params


class Api(object):
    access_key = None
    secret_key = None

    def __init__(self, access_key=None, secret_key=None):
        self.access_key = access_key
        self.secret_key = secret_key

    # Public APIs
    def ticker(self):
        return fetch_public(urls.TICKER)

    def trade(self, params={}):
        return fetch_public(urls.TRADE, params)

    def order_books(self):
        return fetch_public(urls.ORDER_BOOKS)

    def rate(self, params={}):
        return fetch_public(urls.RATE, params)

    def selling_rate(self, pair=''):
        p = '' if pair == '' else '/{}'.format(pair)
        return fetch_public(''.join([urls.SELLING_RATE, p]))

    # Private APIs
    def orders(self, params={}):
        return create_private(urls.ORDERS, params, access_key=self.access_key, secret_key=self.secret_key)

    def opens(self):
        return fetch_private(urls.OPENS, access_key=self.access_key, secret_key=self.secret_key)

    def cancel(self, id=''):
        i = '' if id == '' else '/{}'.format(id)
        return delete_private(''.join([urls.ORDERS, i]))

    def transactions(self):
        return fetch_private(urls.TRANSACTIONS, access_key=self.access_key, secret_key=self.secret_key)

    def transactions_pagination(self):
        return fetch_private(urls.TRANSACTIONS_PAGINATION, access_key=self.access_key, secret_key=self.secret_key)

    def positions(self):
        return fetch_private(urls.POSITIONS, access_key=self.access_key, secret_key=self.secret_key)

    def balance(self):
        return fetch_private(urls.BALANCE, access_key=self.access_key, secret_key=self.secret_key)

    def leverage_balance(self):
        return fetch_private(urls.LEVERAGE_BALANCE, access_key=self.access_key, secret_key=self.secret_key)

    def send_money(self, params={}):
        return create_private(urls.SEND_MONEY, params, access_key=self.access_key, secret_key=self.secret_key)

    def send_money_history(self, params={}):
        p = build_params(params)
        return fetch_private(''.join([urls.SEND_MONEY, p]), access_key=self.access_key, secret_key=self.secret_key)

    def deposit_money_history(self, params={}):
        p = build_params(params)
        return fetch_private(''.join([urls.DEPOSIT_MONEY, p]), access_key=self.access_key, secret_key=self.secret_key)

    def deposit_money_fast(self, id=''):
        u = urls.DEPOSIT_MONEY_FAST.replace(':id', id)
        return create_private(u, access_key=self.access_key, secret_key=self.secret_key)

    def accounts(self):
        return fetch_private(urls.ACCOUNTS, access_key=self.access_key, secret_key=self.secret_key)

    def bank_accounts(self):
        return fetch_private(urls.BANK_ACCOUNTS, access_key=self.access_key, secret_key=self.secret_key)

    def bank_accounts_register(self, params={}):
        return create_private(urls.BANK_ACCOUNTS, params, access_key=self.access_key, secret_key=self.secret_key)

    def bank_accounts_delete(self, id=''):
        u = urls.BANK_ACCOUNTS_DELETE.replace(':id', id)
        return delete_private(u, access_key=self.access_key, secret_key=self.secret_key)

    def withdraws(self):
        return fetch_private(urls.WITHDRAWS, access_key=self.access_key, secret_key=self.secret_key)

    def withdraws_create(self, params={}):
        return create_private(urls.WITHDRAWS, params, access_key=self.access_key, secret_key=self.secret_key)

    def withdraws_delete(self, id=''):
        u = urls.WITHDRAWS_DELETE.replace(':id', id)
        return delete_private(u, access_key=self.access_key, secret_key=self.secret_key)

    def borrows(self, params={}):
        return create_private(urls.BORROWS, params, access_key=self.access_key, secret_key=self.secret_key)

    def matches(self):
        return fetch_private(urls.MATCHES, access_key=self.access_key, secret_key=self.secret_key)

    def repay(self, id=''):
        u = urls.REPAY.replace(':id', id)
        return create_private(u, access_key=self.access_key, secret_key=self.secret_key)

    def to_leverage(self, params={}):
        return fetch_private(urls.TO_LEVERAGE, params, access_key=self.access_key, secret_key=self.secret_key)

    def from_leverage(self, params={}):
        return create_private(urls.FROM_LEVERAGE, params, access_key=self.access_key, secret_key=self.secret_key)


if __name__ == '__main__':
    ak = os.getenv('COINCHECK_ACCESS_KEY', '')
    sk = os.getenv('COINCHECK_SECRET_KEY', '')
    api = Api(ak, sk)

    r = api.ticker()
    print(r)

    r = api.trade({
        'offset': 0
    })
    print(r)

    r = api.order_books()
    print(r)

    r = api.rate({
        'order_type': 'sell',
        'pair': 'btc_jpy',
        'amount': '1'
    })
    print(r)

    r = api.selling_rate('btc_jpy')
    print(r)

    # r = api.orders()
    # print(r)

    r = api.opens()
    print(r)

    # r = api.cancel('')
    # print(r)

    r = api.transactions()
    print(r)

    r = api.transactions_pagination()
    print(r)

    r = api.positions()
    print(r)

    r = api.balance()
    print(r)

    r = api.leverage_balance()
    print(r)

    # r = api.send_money({
    #     'address': '',
    #     'amount': 1
    # })
    # print(r)

    r = api.send_money_history({
        'currency': 'btc'
    })
    print(r)

    r = api.deposit_money_history({
        'currency': 'btc'
    })
    print(r)

    # r = api.deposit_money_fast('334')
    # print(r)

    r = api.accounts()
    print(r)

    # r = api.bank_accounts()
    # print(r)

    # r = api.bank_accounts_register({})
    # print(r)

    # r = api.bank_accounts_delete('')
    # print(r)

    # r = api.withdraws()
    # print(r)

    # r = api.withdraws_create({})
    # print(r)

    # r = api.withdraws_delete('')
    # print(r)

    # r = api.borrows({})
    # print(r)

    # r = api.matches()
    # print(r)

    # r = api.repay('')
    # print(r)

    # r = api.to_leverage({})
    # print(r)

    # r = api.from_leverage({})
    # print(r)
