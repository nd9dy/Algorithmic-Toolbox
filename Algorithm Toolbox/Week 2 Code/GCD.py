# Uses python3
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
print(gcd_naive(a, b))
