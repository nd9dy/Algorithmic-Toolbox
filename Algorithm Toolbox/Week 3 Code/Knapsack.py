# Uses python3
from operator import itemgetter
def get_optimal_value(s, max, whole):
    value = 0
    b = 0
    while b == 0:
        if max == whole[s][1]:
            value += whole[s][0]
            b = 1
        elif  max > whole[s][1] and s == 0:
            value += whole[s][0]
            b = 1
        elif max < whole[s][1]:
            value += max * whole[s][2]
            b = 1
        else:
            value += whole[s][0]
            max -= whole[s][1]
            s -= 1
    return value

x = []
x = input().split()
whole = []
s = int(x[0])
max = int(x[1])
for i in range(s):
    data = list(map(int, input().split()))
    data.append(data[0]/data[1])
    whole.append(data)
whole = sorted(whole, key=itemgetter(2))
real = get_optimal_value(s-1, max, whole)
print("{:.4f}".format(real))
