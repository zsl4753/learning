'''
初始代码，耗时较多
'''
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
'''
代码优化
'''
import time
import math

start = time.clock()

for num in range(1,10000):
    sum = 0
    for factor in range(1,int(math.sqrt(num))+1):
        if num%factor == 0:
            sum =sum+factor
            if factor >1 and num/factor !=factor:
                sum = sum+ num/factor
    if sum == num and num!= 1:
        print(num)
end = time.clock()
print(end-start)
