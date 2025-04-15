
# Quadratzahlen

"""
Schreibe ein Skript, welches alle Quadratzahlen von natürlichen
Zahlen (1, 2, 3, ...) ausgibt, die kleiner als 100 sind.
(Die Quadratzahlen sollen kleiner 100 sein!)

Zusatz: Gib auch die Anzahl der gefundenen Quadratzahlen aus
"""
from math import sqrt

def list_squares_under(num :int) -> list:
    return [x**2 for x in range(1, int(sqrt(100)))]

if __name__ == '__main__':
    squrs = list_squares_under(100)
    print(len(squrs), " Quadratzahlen gefunden: ", squrs)