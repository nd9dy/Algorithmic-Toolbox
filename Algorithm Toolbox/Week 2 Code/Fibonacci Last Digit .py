# Uses python3
def calc_fib(n):
    list = [1,1]
    now = []
    if n < 2:
        return n
    else:
        for i in range(2,n):
            new = list[i-1] % 10 + list[i-2] % 10
            list.append(new)
        last = list[-1]
        return last % 10


n = int(input())
print(calc_fib(n))
