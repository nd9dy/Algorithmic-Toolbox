# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    i = l
    j = r
    
    while True:
        if a[i] >= x and a[j] <= x:
          if i < j:
            a[i],a[j] = a[j],a[i]
            i += 1
            j -= 1

          else:
            return j


        if a[j] > x:
          j -= 1

        if a[i] < x:
          i += 1




def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition3(a, l, r)
    randomized_quick_sort(a, l, m);
    randomized_quick_sort(a, m + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
