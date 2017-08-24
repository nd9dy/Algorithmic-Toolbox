# Uses python3
def get_change(m):
    count = 0
    if m < 5:
        return m
    else:
        x = 0
        while True:
            if m == 0:
                break
            else:
                if m >= 10:
                    m -= 10
                    count += 1
                    x += 1
                elif 5 <= m < 10:
                    m -= 5
                    count += 1
                else:
                    count += m
                    m -= m
        return count



m = int(input())
print(get_change(m))
