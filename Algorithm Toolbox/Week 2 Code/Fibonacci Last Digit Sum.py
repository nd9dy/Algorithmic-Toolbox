# Uses python3
import sys

def fibonacci_sum_naive(n):
    list = [0, 1, 1]
    if n < 2:
        return n
    else:
        i = 3
        while True:
            if list[i - 1] == 1 and list[i - 2] == 0:
                break
            new = (list[i - 1] % 10) + (list[i - 2] % 10)
            real = new % 10
            list.append(real)
            i += 1
        length = len(list) - 2
        if list[(n+2)%length] - 1 == -1:
            return 9

        else:
            return list[(n+2)%length] - 1
n = int(input())
print(fibonacci_sum_naive(n))
