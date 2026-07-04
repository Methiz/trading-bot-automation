# ============ CORE MARKET ANALYSIS BRAIN ============
def analyze_market_brain(pair, df_2m=None, df_5m=None, df_15m=None):

    if datetime.now(UTC).weekday() >= 5:
        print("\n===============================\n🚫 MARKET CLOSED (Weekend)\n===============================\n")
        return {"status": "skip", "reason": "Weekend - Market Closed"}

    print(f"[ANALYSIS START] {pair}")
