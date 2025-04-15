
# Fakultät

"""
Schreibe ein Skript, dass ermittelt,
welche Zahl möglichst groß ist
ohne dass ihre Fakultät über 1.000.000.000 ist.

Hinweis:
Fakultät von 5 (Kurzschreibweise: 5!):
1 * 2 * 3 * 4 * 5 = 120
"""

from X010_factorial import factorial_iterative

def find_greatest_under_factorial(limit :int) -> int:
   x = 1
   while factorial_iterative(x + 1) <= limit:
       x += 1
   return x

if __name__ == "__main__":
    print(find_greatest_under_factorial(1_000_000_000))
