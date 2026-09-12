import ccxt
import time
import os

API_KEY = os.environ.get('BINANCE_API_KEY')
API_SECRET = os.environ.get('BINANCE_API_SECRET')

exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'enableRateLimit': True,
})

SYMBOL = 'ETH/USDT'
GRID_LEVELS = 5
GRID_SPACING = 0.01
ORDER_SIZE = 0.01

print("Bot başladı. 24/7 çalışıyor...")

while True:
    try:
        ticker = exchange.fetch_ticker(SYMBOL)
        price = ticker['last']
        print(f"ETH Fiyatı: {price}")
        time.sleep(60)
    except Exception as e:
        print(f"Hata: {e}")
        time.sleep(60)
