# Uses python3
def max_dot_product(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

store = input()
real = input()
maybe = input()
a = list(map(int, real.split()))
a = sorted(a,reverse=True)
b = list(map(int, maybe.split()))
b = sorted(b,reverse=True)
print(max_dot_product(a, b))

