# Uses python3
from decimal import Decimal
def gcd_naive(a, b):
    x = 5
    while x > 1:
        if a % b != 0:
            c = a % b
            a = b
            b = c
        else:
            x = 1
    return b

there = input()
store = there.split()
a = int(max(store))
b = int(min(store))
factor = gcd_naive(a,b)
if factor > 1:
    multiple = (Decimal(a) * Decimal(b)) / Decimal(factor)
else:
    multiple = Decimal(a * b)

print(int(multiple))
