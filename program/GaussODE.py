import sympy as sp

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
    f2 = z ** (-m) * sp.summation(sp.rf(a - m, n) * sp.rf(b - m, n) / (sp.factorial(n) * sp.rf(1 - m, n)), (n, 0, m - 1))
    f3 = ((-1) ** (m - 1) / sp.factorial(m - 1)) * sp.summation(
        (sp.rf(a - m, m) * sp.rf(b - m, m) * z ** (n - m) / (sp.factorial(n) * sp.factorial(n - m))) * (
            H(m - 1) - H(n) - H(n - m) + sp.summation(1 / (a - m + k) + 1 / (b - m + k), (k, 0, n - 1))), (n, m, sp.oo))
    return f3


a = 2
b = 2
m = 1
c = 1 + m
w = sp.hyper((a, b), [c], z)
print(sp.simplify(L(a, b, c, w)))
print(w2(a, b, m, z))
