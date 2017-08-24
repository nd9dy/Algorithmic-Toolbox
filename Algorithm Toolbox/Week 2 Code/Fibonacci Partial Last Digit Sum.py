# Uses python3
import sys

them = [0,1,1]
i = 3
while True:
    if them[i - 1] == 1 and them[i - 2] == 0:
        break
    new = (them[i - 1] % 10) + (them[i - 2] % 10)
    real = new % 10
    them.append(real)
    i += 1



def fibonacci_sum_naive(n,m):
    global them
    if n == m:
        if n < 2:
            return n
        else:
            yam = them
            length = len(yam) - 2
            if yam[n % length]  == -1:
                return 9

            else:
                return yam[n % length]
    else:
        raw = them
        length = len(raw) - 2
        maybe = raw[(m+2) % length] - 1
        compare = raw[(n + 1) % length] - 1
        if maybe < compare:
            return (maybe + 10) - compare
        else:
            return maybe - compare



store = input()
n , m = map(int, store.split())
print(fibonacci_sum_naive(n, m))
