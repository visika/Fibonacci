# Fibonacci #
from sys import argv
from math import sqrt

script, n = argv

n = int(n)
c1 = (sqrt(5) - 1) / (2 * sqrt(5))
c2 = (sqrt(5) + 1) / (2 * sqrt(5))

def f(x):
    fibo = c1 * ((1 - sqrt(5)) / 2)**x + c2 * ((1 + sqrt(5)) / 2)**x
    print int(round(fibo))

f(n)
