def yueshu(x):
    ys = []
    sum = 0
    for i in range(2,x+1):
        ys1 = x /i
        if ys1 == int(ys1):
            ys.append(ys1)
    for i in ys:
            sum = sum+i
    return sum

for x in range(2,10000):
    if yueshu(x) == x:
print(x)
