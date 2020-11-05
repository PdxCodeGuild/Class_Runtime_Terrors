import finnhub
import requests
import datetime

finnhub_client = finnhub.Client(api_key= 'buh2utf48v6s9c138qlg')

exchange = input("please type the exchange: ").upper()
resolution = input("resolution (1, 5, 15, 30, 60, D, W, M): ").upper()
base_currancy = input("base currency = ").upper()
quote_currency = input("quote currency = ").upper()


print(quote_currency + base_currancy)
print (exchange)
print (resolution)

def symbol_clarity(exchange, base_currancy, quote_currency):
    if exchange == "KRAKEN":
        kraken_symbol = quote_currency + base_currancy
        if quote_currency == "ETH":
            kraken_symbol = "X"+kraken_symbol
        return kraken_symbol
        # look up required syntax
    elif exchange == "GEMINI":
        return gemini_symbol
    elif exchange == "BINANCE":
        binance_symbol = quote_currency + base_currancy
        return binance_symbol
symbol_clarity = symbol_clarity(exchange, base_currancy, quote_currency)
print(symbol_clarity)

# UNIX required for intial and end of candle

time = datetime.datetime.utcnow().timestamp()
print (time)

# .get f string needs to be compiled according to input variables

r = requests.get(f'https://finnhub.io/api/v1/crypto/candle?symbol={exchange}:{symbol_clarity}&resolution=D&from=1572651390&to=1575243390&token=buh2utf48v6s9c138qlg')
print(r.json())


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
# print (finnhub_client.crypto_candles('KRAKEN:XETHXXBT', 'D', 1590988249, 1591852249))



