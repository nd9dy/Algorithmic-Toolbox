# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
a = sorted(a)
uno = max(a)
t = 0
for i in range(len(a)):
    if a[i] == uno:
        t += 1
if t > 1:
    second = uno * uno
else:
    dos = sorted(a)[-2]
    second = uno * dos
print(second)
              





 
