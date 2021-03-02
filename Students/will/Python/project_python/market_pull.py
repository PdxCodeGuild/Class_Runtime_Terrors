import finnhub
import requests
import datetime

finnhub_client = finnhub.Client(api_key= 'buh2utf48v6s9c138qlg')

# exchange = input(""" 

# Exchange = """).upper()
# base_currancy = input(" Base currency = ").upper()
# quote_currency = input(" Quote currency = ").upper()
# resolution = input(" Candle resolution (1, 5, 15, 30, 60, D, W, M) = ").upper()
# # back_time = input(" Candle QTY = ")
# # back_time = int(back_time)
# # time_sec = {'1': 60, '5': 300, '15': 900, '30': 1800, '60': 3600, 'D':86400, 'W': 604800, 'M':2680000}
# # print(back_time)
# print(quote_currency + base_currancy)
# print (exchange)
# print (resolution)

# def exchange_symbol_clarity(exchange, base_currancy, quote_currency):
#     if exchange == "KRAKEN":
#         kraken_symbol = "X" + quote_currency + "X" + base_currancy
#         return kraken_symbol
#         # look up required syntax
#     elif exchange == "GEMINI":
#         return gemini_symbol
#     elif exchange == "BINANCE":
#         binance_symbol = quote_currency + base_currancy
#         return binance_symbol
# exchange_symbol_clarity = exchange_symbol_clarity(exchange, base_currancy, quote_currency)

# # UNIX required for intial and end of candle

time = int(datetime.datetime.utcnow().timestamp())
time_less = time - 18100
print (time_less)
print (time)
candle = finnhub_client.crypto_candles('KRAKEN:XETHXXBT', '1', time_less, time)
print (candle)
print (1604721600 - 1604654399)
# .get f string needs to be compiled according to input variables

# r = requests.get(f'https://finnhub.io/api/v1/crypto/candle?symbol={exchange}:{exchange_symbol_clarity}&resolution={resolution}&from={time_less}&to={time}&token=buh2utf48v6s9c138qlg')
# print(r.json())
# for item in r:
#         print(item)
# Crypto Exchange
# print(finnhub_client.crypto_exchanges())

# Crypto symbols
# print(finnhub_client.crypto_symbols(f'{exchange}'))

# Crypto Candles
# symbol = (f"{exchange}:{symbol_clarity}")
# print(symbol)


# for symbol in finnhub_client.crypto_symbols(f'{exchange}'):
#     if symbol == symbol:
#         print(symbol)

# print(finnhub_client.crypto_candles(symbol, resolution, 1590988249, 1591852249))

# time = int(datetime.datetime.utcnow().timestamp())
# start_time = int(time - 60)

# print(start_time)
# print (time)

# #print(finnhub_client.crypto_candles('BINANCE:BTCUSDT', 'D', 1590988249, 1591852249))



