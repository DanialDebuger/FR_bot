import requests
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO

API_KEY = "a89be4d0613b43bdb31ff3498b8725c8"

def get_analysis(symbol):
    url = f"https://api.twelvedata.com/time_series?symbol={symbol}&interval=15min&outputsize=50&apikey={API_KEY}"
    r = requests.get(url).json()
    values = r.get("values", [])

    if not values:
        return f"داده‌ای برای {symbol} پیدا نشد."

    df = pd.DataFrame(values)
    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.sort_values("datetime")
    df["close"] = pd.to_numeric(df["close"])
    ema = df["close"].ewm(span=20).mean().iloc[-1]
    current_price = df["close"].iloc[-1]

    return f"تحلیل {symbol}:
قیمت فعلی: {current_price:.4f}
EMA20: {ema:.4f}"

def generate_chart(symbol, api_key):
    url = f"https://api.twelvedata.com/time_series?symbol={symbol}&interval=15min&outputsize=50&apikey={api_key}"
    r = requests.get(url).json()
    values = r.get("values", [])

    if not values:
        return None

    df = pd.DataFrame(values)
    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.sort_values("datetime")
    df["close"] = pd.to_numeric(df["close"])
    df["ema"] = df["close"].ewm(span=20).mean()

    plt.figure(figsize=(10, 4))
    plt.plot(df["datetime"], df["close"], label="Price", color="blue")
    plt.plot(df["datetime"], df["ema"], label="EMA20", color="orange", linestyle="--")
    plt.title(f"{symbol} - 15min Chart")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()
    return buffer