
# Zwei Zahlen genau vergleichen

# Schreibe ein Programm, das testet und ausgibt,
# welche von zwei Zahlen größer ist oder ob beide Zahlen gleich groß sind.
# Die beiden Zahlen sollen zufällig erzeugt werden.

from random import randint

def max_of(a, b) -> int:
    return [[-1, 1], [0]][a==b][a>b]

def max_of_randints(min :int, max :int) -> None:
    a, b = randint(min, max), randint(min, max)
    res = [["genauso groß wie"],["kleiner als", "größer als"]]
    print(a, " ist ", res[max_of(a, b)][max_of(a, b) > 0], b)


if __name__ == "__main__":
    for i in range(10):
        max_of_randints(1, 5)
