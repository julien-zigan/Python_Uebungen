
# Zwei Zahlen genau vergleichen

# Schreibe ein Programm, das testet und ausgibt,
# welche von zwei Zahlen größer ist oder ob beide Zahlen gleich groß sind.
# Die beiden Zahlen sollen zufällig erzeugt werden.

from random import randint

class Comparator:
    def __init__(self):
        self.LT = "kleiner als"
        self.GT = "größer als"
        self.EQ = "genause groß wie"

    def max_of(self, a, b) -> int:
        return [[-1, 1], [0]][a==b][a>b]

    def max_of_randints(self, min :int, max :int) -> None:
        a, b = randint(min, max), randint(min, max)
        res = [[self.EQ],[self.LT, self.GT]]
        print(a, " ist ", res[self.max_of(a, b)][self.max_of(a, b) > 0], b)


if __name__ == "__main__":
    for i in range(10):
        comp = Comparator()
        comp.max_of_randints(1, 5)
