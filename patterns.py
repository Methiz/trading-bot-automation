# ============ COMPLETE 36 CANDLESTICK PSYCHOLOGY ENGINE ============
def detect_all_candles(df):
    if len(df) < 5:
        return ["Standard Candle"]
    
    body_series = abs(df['Close'] - df['Open'])
    avg_body = body_series.rolling(5).mean().iloc[-2]

    O, H, L, C = float(df['Open'].iloc[-1]), float(df['High'].iloc[-1]), float(df['Low'].iloc[-1]), float(df['Close'].iloc[-1])
    pO, pH, pL, pC = float(df['Open'].iloc[-2]), float(df['High'].iloc[-2]), float(df['Low'].iloc[-2]), float(df['Close'].iloc[-2])
    ppO, ppH, ppL, ppC = float(df['Open'].iloc[-3]), float(df['High'].iloc[-3]), float(df['Low'].iloc[-3]), float(df['Close'].iloc[-3])
