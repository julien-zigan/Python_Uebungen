
# Binäre Zahlen

# Schreibe ein Skript, das alle Zahlen von 0-255 binär schreibt:
# Beachte die Leerzeichen zwischen den Ziffern!

"""
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1
0 0 0 0 0 0 1 0
0 0 0 0 0 0 1 1
0 0 0 0 0 1 0 0
...
...
...
1 1 1 1 1 0 1 1
1 1 1 1 1 1 0 0
1 1 1 1 1 1 0 1
1 1 1 1 1 1 1 0
1 1 1 1 1 1 1 1
"""
from math import log


def print_binaries(limit: int) -> None:
    places = int(log(limit, 2))
    for i in range(1, limit, 2):
        for j in range(1, places):
            print(1 if i & limit>>j else 0, end=" ")
        print()


if __name__ == "__main__":
    print_binaries(256)

