# Uses python3
import math, sys
def binary_search(first,item):
    n = 0
    check = math.log(len(first),2)
    left, right = 0, len(first) - 1
    while True:
        mid = left + ((right - left) / 2)
        mid = int(mid)
        if item == first[mid]:
            return mid
        if n > check:
            return -1
        elif item > first[mid]:
            left = mid + 1
            n += 1
        elif item < first[mid]:
            right = mid - 1
            n += 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n+1]
    first = data[1:n+1]
    second = data[n+2:]
    storage = []
    for item in second:
        storage.append(binary_search(first,item))
    print( " ".join(map(str,storage)))
