BASE = 'https://coincheck.com'
API = BASE + '/api'

# Public API
# Ticker
TICKER = API + '/ticker'
# Trade
TRADE = API + '/trades'
# Order books
ORDER_BOOKS = API + '/order_books'
# Rate
RATE = API + '/exchange/orders/rate'
# Selling rate
SELLING_RATE = API + '/rate'

# Private API
# Orders
ORDERS = API + '/exchange/orders'  # uses create, delete
OPENS = API + '/exchange/orders/opens'
TRANSACTIONS = API + '/exchange/orders/transactions'
TRANSACTIONS_PAGINATION = API + '/exchange/orders/transactions_pagination'
POSITIONS = API + '/exchange/leverage/positions'
# Accounts
BALANCE = API + '/accounts/balance'
LEVERAGE_BALANCE = API + '/accounts/leverage_balance'
SEND_MONEY = API + '/send_money'  # uses create, fetch
DEPOSIT_MONEY = API + '/deposit_money'
DEPOSIT_MONEY_FAST = API + '/deposit_money/:id/fast'
ACCOUNTS = API + '/accounts'
# Banks
BANK_ACCOUNTS = API + '/bank_accounts'  # uses create, fetch
BANK_ACCOUNTS_DELETE = BANK_ACCOUNTS + '/:id'
WITHDRAWS = API + '/withdraws'  # uses create, fetch
WITHDRAWS_DELETE = WITHDRAWS + '/:id'
# Margin order
BORROWS = API + '/lending/borrows'
MATCHES = BORROWS + '/matches'
REPAY = BORROWS + '/:id/repay'
# Leverage Transfer
TO_LEVERAGE = API + '/exchange/transfers/to_leverage'
FROM_LEVERAGE = API + '/exchange/transfers/from_leverage'


