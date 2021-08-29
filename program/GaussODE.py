import sympy as sp
import time
import random

start_time = time.time()

(a, b, c, m, n, k) = sp.var('a, b, c, m, n, k')
z = sp.Symbol('z')
w = sp.Function('w')(z)


def L(a, b, c, w):
    return z * (1 - z) * sp.diff(w, z, 2) + (c - (a + b + 1) * z) * sp.diff(w, z) - a * b * w


def H(n):
    return sp.harmonic(n)


def w2(a, b, m, z):
    w1 = sp.hyper((a, b), [c], z)
    f1 = w1 * sp.ln(z) * (-1) ** (m - 1) * sp.rf(a - m, m) * sp.rf(b - m, m) / (sp.factorial(m) * sp.factorial(m - 1))
    f2 = z ** (-m) * sp.summation(sp.rf(a - m, n) * sp.rf(b - m, n) * z ** n / (sp.factorial(n) * sp.rf(1 - m, n)), (n, 0, m - 1))
    f3 = ((-1) ** (m - 1) / sp.factorial(m - 1)) * sp.summation(
        (sp.rf(a - m, n) * sp.rf(b - m, n) * z ** (n - m) / (sp.factorial(n) * sp.factorial(n - m))) * (
            H(m - 1) - H(n) - H(n - m) + sp.summation(1 / (a - m + k) + 1 / (b - m + k), (k, 0, n - 1))), (n, m, 64))
    return f1 + f2 + f3


m = 7
c = 1 + m
W = w2(a, b, m, z)
F = L(a, b, c, W)

for _ in range(10):
    a_ = random.uniform(-4, 4) * 4
    b_ = random.uniform(-4, 4) * 4
    print("a:", a_, " b:", b_)
    for p in range(2, 10):
        print(F.subs([(a, a_), (b, b_), (z, 1 / p)]).evalf())
    print("--------------------------------")

print("time :", time.time() - start_time)
