# Uses python3
import sys

def calc_fib(n,m):
    list = [0,1,1]
    i = 3
    while True:
        if list[i-1] == 1 and list[i-2] == 0:
            break
        new = (list[i - 1] % m) + (list[i - 2] % m)
        real = new % m
        list.append(real)
        i += 1
    length = len(list) - 2
    return list[n%length]



store = input()
n,m = map(int, store.split())
print(calc_fib(n,m))
