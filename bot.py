import os
import time
from pybit.unified_trading import HTTP
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BYBIT_API_KEY")
API_SECRET = os.getenv("BYBIT_API_SECRET")

# === AYARLAR ===
SYMBOL = "ETHUSDT" # Hangi parite
GRID_COUNT = 10 # Toplam 10 kademe: 5 altta 5 üstte
GRID_SPACING_PCT = 0.005 # %0.5 aralık. %1 için 0.01 yaz
ORDER_QTY_USDT = 10 # Her emir 10 USDT'lik
LEVERAGE = 3 # Kaldıraç
# ===============

client = HTTP(
    testnet=False, # Test için True. Gerçek para için False
    api_key=API_KEY,
    api_secret=API_SECRET,
)

def set_leverage():
    try:
        client.set_leverage(category="linear", symbol=SYMBOL, buyLeverage=str(LEVERAGE), sellLeverage=str(LEVERAGE))
        print(f"Kaldıraç {LEVERAGE}x ayarlandı")
    except Exception as e:
        print("Kaldıraç hatası:", e)

def get_price():
    ticker = client.get_tickers(category="linear", symbol=SYMBOL)
    return float(ticker["result"]["list"][0]["lastPrice"])

def place_grid_orders(mid_price):
    print(f"Orta fiyat: {mid_price}")
    
    try:
        client.cancel_all_orders(category="linear", symbol=SYMBOL)
        time.sleep(1)
    except: pass
    
    for i in range(1, GRID_COUNT + 1):
        buy_price = mid_price * (1 - GRID_SP
