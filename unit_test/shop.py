# shop.py
def berechne_rabatt(preis, prozent):
    if prozent < 0 or prozent > 100:
        raise ValueError("Ungültiger Rabatt")
    return preis * (1 - prozent / 100)
