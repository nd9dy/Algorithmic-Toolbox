# Uses python3
def calc_fib(n):
    list = [1,1]
    if n < 2:
        return n
    else:
        for i in range(2,n):
            new = list[i-1] + list[i-2]
            list.append(new)
        return list[-1]


n = int(input())
print(calc_fib(n))
