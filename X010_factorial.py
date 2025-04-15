import sys

sys.setrecursionlimit(int(1E8))

def factorial_recursive(n :int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def factorial_iterative(n :int) -> int:
    x = 1
    for i in range(n):
        x *= i + 1
    return x

def n_choose_k(n :int, k :int) -> float:
    return factorial_iterative(n) / (factorial_iterative(k) * factorial_iterative(n - k))

def german_lotto_probability() -> float:
    return 100 / n_choose_k(49, 6)


if __name__ == '__main__':
    print("Gewinnchancen bei 6 aus 49: {0:.9f} ".format(german_lotto_probability()))