'''
Для анализа собственных движений цены фьючерса ETHUSDT необходимо исключить из неё влияние цены BTCUSDT.
Для этого можно использовать анализ корреляции, чтобы оценить степень зависимости двух ценных бумаг.
Если значение корреляции превышает заданный порог, то можно сделать вывод, что изменение цены одной ценной бумаги
может иметь влияние на изменение цены другой. Таким образом, анализ корреляции может помочь исключить из движений
цены фьючерса ETHUSDT
'''

import requests
import json
import time

WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'

# Get the price of ETHUSDT and BTCUSDT
url = 'https://www.binance.com/api/v3/ticker/price'
eth = {'symbol': 'ETHUSDT'}
btc = {'symbol': 'BTCUSDT'}

# Continue to read the actual price
while True:
    response_eth = requests.get(url, params=eth)
    response_btc = requests.get(url, params=btc)

    data_eth = json.loads(response_eth.text)
    data_btc = json.loads(response_btc.text)

    eth_price = float(data_eth['price'])
    btc_price = float(data_btc['price'])
    color = GREEN
    print(f"ETH: {color}{eth_price}{WHITE} / BTC: {color}{btc_price}{WHITE}")
    eth_diff = eth_price - btc_price

    try:
        eth_change = abs(eth_diff - eth_diff) / eth_diff
        if eth_change > 0.01:
            print('The price of ETHUSDT has changed by more than 1% over the last 60 minutes.')
    except ZeroDivisionError as e:
        print(e)
        continue

    eth_change = (eth_diff - eth_diff)/eth_diff
    color = RED
    print(f"eth_change: {color}{eth_change}{WHITE} / eth_diff: {color}{eth_diff}{WHITE}")
    time.sleep(3)
