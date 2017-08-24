# Uses python3
import sys

def optimal_sequence(n):
    man = [0,0,1,1]
    y = n
    check = []
    x = 4
    if n > 3:
        while True:
            if len(man) == n+1:
                break
            else:
                if x % 6 ==0:
                    man.append(min(man[x//2],man[x//3],man[x-1]) + 1)
                    x += 1
                elif x % 3 == 0:
                    man.append(min(man[x//3],man[x-1]) + 1)
                    x += 1
                elif x % 2 == 0:
                    man.append(min(man[x//2],man[x-1]) + 1)
                    x += 1
                else:
                    man.append(man[x-1]+1)
                    x += 1

    while True:
        if y > 0:
            check.append(y)
            risk = min(man[y-1],man[y//2],man[y//3])
            beta = min(man[y-1],man[y//2])
            alpha = min(man[y-1],man[y//3])
            if y % 6 == 0:
                if risk == man[y - 1]:
                    y -= 1
                elif risk == man[y // 3]:
                    y = y // 3
                else:
                    y = y // 2
            elif y % 2 == 0 and y % 3 != 0:
                if beta == man[y - 1]:
                    y -= 1
                else:
                    y = y // 2
            elif y % 3 == 0 and y % 2 != 0:
                if alpha == man[y - 1]:
                    y -= 1
                else:
                    y = y // 3
            else:
                y -= 1
        
        else:
            break



    return reversed(check)



input = sys.stdin.read()
n = int(input)
main = list(optimal_sequence(n))
print((len(main) - 1))     
for x in main:
    print(x, end=' ')
