# Uses python3
import sys

def get_majority_element(a,n):
    a = sorted(a)
    y = int(n / 2)
    check = a[y]
    count = 0
    for i in range(len(a)):
        if count > y:
            return 0
        elif check == a[i]:
            count += 1

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, n) != -1:
        print(1)
    else:
        print(0)

