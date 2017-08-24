# Uses python3

def evalt(a, b, op):
    if op == '+':
        return int(a)+int(b)
    elif op == '-':
        return int(a)-int(b)
    elif op == '*':
        return int(a)*int(b)
    else:
        assert False


def maximumvalue(dataset):
    if len(dataset) == 3:
        x = int(dataset[0])
        y = int(dataset[2])
        return evalt(x,y,dataset[1])

    check = (len(dataset) // 2) + 1
    minlist = []
    maxlist = []
    operand = []
    
    for i in range(0,len(dataset)):
        if i % 2 == 0:
            minlist.append(dataset[i])
            maxlist.append(dataset[i])
        else:
            operand.append(dataset[i])


    for i in range(0,len(dataset)):
        if i % 2 ==0 and i > 0:
            minlist.append(evalt(dataset[i-2],dataset[i],dataset[i-1]))
            maxlist.append(evalt(dataset[i-2],dataset[i],dataset[i-1]))

    for s in range(0,check):
        for i in range(0,check - s):
            j = i + s
            if j > i + 1:
                first, second = MinandMax(i,j,minlist,maxlist,operand,real)
                minlist.append(first)
                maxlist.append(second)


    return maxlist[-1]



def MinandMax(i,j,minlist,maxlist,operand,real):
    maximum = -100000000000000000000000000000000000
    minimum = 10000000000000000000000000000000000000
    for k in range(i,j):
        reg = i + real[k-i]
        chill = k + 1 + real[j-k-1]
        a = evalt(maxlist[reg],maxlist[chill],operand[k])
        b = evalt(maxlist[reg],minlist[chill],operand[k])
        c = evalt(minlist[reg],maxlist[chill],operand[k])
        d = evalt(minlist[reg],minlist[chill],operand[k])
        minimum = min(minimum,a,b,c,d)
        maximum = max(maximum,a,b,c,d)
    return minimum,maximum




dataset = list(input())
real = [0]
x = (len(dataset) // 2) + 1
y = 0
for i in range(0,len(dataset)//2):
    real.append(x+y)
    x -= 1
    y = real[-1]

print(maximumvalue(dataset))
