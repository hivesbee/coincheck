import datetime

import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib import ticker

from models import Ticker


def create_candles(interval=30, type='ask'):
    tickers = Ticker.select().order_by(Ticker.timestamp.desc())
    print(len(tickers))
    print(tickers[0].timestamp.timestamp())
    print(tickers[-1].timestamp.timestamp())

    origin = tickers[0].timestamp.timestamp()

    times = []
    candles = []
    group = []

    for t in tickers:
        if origin >= t.timestamp.timestamp() > origin - interval:
            group.append(t.ask if type == 'ask' else t.bid)
        else:
            if 0 < len(group):
                times.append(origin)
                # candles.append((datetime.datetime.fromtimestamp(origin), group[-1], max(group), min(group),  group[0]))
                candles.append((origin, group[-1], max(group), min(group),  group[0]))

            group = []

            origin -= interval

    t = [x for x in reversed(times)]
    cdl = [x for x in reversed(candles)]

    [print(c) for c in candles]

    # 描画
    # d = [x[0] for x in candles]
    # o = [x[1] for x in candles]
    # h = [x[2] for x in candles]
    # l = [x[3] for x in candles]
    # c = [x[4] for x in candles]

    # x = d, o, h, l, c
    # ohlc = []
    # ohlc.append(x)


    fig, ax = plt.subplots()
    # candlestick_ohlc(ax, cdl, width=(1.0 / 24 / 60 * interval), colorup='b', colordown='r')
    candlestick_ohlc(ax, cdl)

    xdate = [datetime.datetime.fromtimestamp(i) for i in t]
    # ax.xaxis.set_major_locator(ticker.MaxNLocator(1))

    def mydate(x, pos):
        try:
            return xdate[int(x)]
        except IndexError:
            return ''

    ax.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))

    fig.autofmt_xdate()
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()


if __name__ == '__main__':
    print('test')

    create_candles(120)
