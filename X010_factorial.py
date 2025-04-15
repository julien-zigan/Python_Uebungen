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
    return 1 / n_choose_k(49, 6)

def eurojackpot_probability() -> float:
    return (1 / n_choose_k(50, 5)) * (1 / n_choose_k(12, 2))


if __name__ == '__main__':
    lp = german_lotto_probability()
    lh = int(1/lp)
    ltxt = "Gewinnchancen für sechs richtige Zahlen (ohne Zusatzzahl) bei 6 aus 49:"
    print(f"{ltxt:75}{lp:.11f} (1:{lh})")
    ep = eurojackpot_probability()
    eh = int(1/ep)
    etxt = "Gewinnchancen bei Eurojackpot (5 aus 50 und 2 aus 12):"
    print(f"{etxt:75}{ep:.11f} (1:{eh})")
