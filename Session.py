def get_session():
    h = datetime.now(timezone.utc).hour
    if 8 <= h < 12: return "LONDON"
    elif 12 <= h < 16: return "LONDON/NY OVERLAP"
    elif 16 <= h < 21: return "NEW YORK"
    else: return "DEAD SESSION"
