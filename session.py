"""
session.py 

Detects the current Forex trading session based on UTC time.
"""

from datetime import datetime, timezone


def get_market_session():
    """
    Returns the active trading session.

    Sessions:
    - London
    - London / New York Overlap
    - New York
    - Off Market
    """

    current_hour = datetime.now(timezone.utc).hour

    if 8 <= current_hour < 12:
        return "London Session"

    elif 12 <= current_hour < 16:
        return "London / New York Overlap"

    elif 16 <= current_hour < 21:
        return "New York Session"

    else:
        return "Off Market"


if __name__ == "__main__":
    session = get_market_session()
    print(f"Current Session: {session}")
