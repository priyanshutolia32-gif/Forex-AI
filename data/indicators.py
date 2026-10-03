import pandas as pd
from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator
from ta.volatility import AverageTrueRange

def add_indicators(data):
    data = data.copy()

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    close = data["Close"]
    high = data["High"]
    low = data["Low"]

    data["EMA_20"] = EMAIndicator(close=close, window=20).ema_indicator()
    data["EMA_50"] = EMAIndicator(close=close, window=50).ema_indicator()
    data["RSI_14"] = RSIIndicator(close=close, window=14).rsi()

    atr = AverageTrueRange(
        high=high,
        low=low,
        close=close,
        window=14
    )
    data["ATR_14"] = atr.average_true_range()

    return data

if __name__ == "__main__":
    from market_data import get_market_data

    data = get_market_data(period="60d", interval="1h")
    data = add_indicators(data)

    print(data[["Close", "EMA_20", "EMA_50", "RSI_14", "ATR_14"]].tail())
