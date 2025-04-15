
# Sternenmuster

# Schreibe ein Python-Programm,
# das folgende Sternchen-Muster auf den Bildschirm schreibt:

"""
* * * *
* * * *
* * * *

*
* *
* * *
* * * *
* * * * *

      *
    * * *
  * * * * *
* * * * * * *
"""

def print_square(height :int, width :int) -> None:
    for i in range(height):
        print("* " * width)

def print_slope(height :int) -> None:
    for i in range(height):
        print("* " * (i+1))

def print_pyramid(height :int) -> None:
    for i in range(height):
        print("  " * (height - i - 1), "* " * (i * 2), "*", sep="")

if __name__ == '__main__':
    print_square(3, 4)
    print()
    print_slope(5)
    print()
    print_pyramid(4)
