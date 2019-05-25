'''
判断一个数是否为素数
'''

from math import sqrt
num = int(input('请输入一个正整数:'))
end = int(sqrt(num))
is_prime = True
for x in range(2,end+1):
    if num%x == 0:
        is_prime = False
        break
if is_prime and num!= 1:
    print("%d是素数"%num)
else:
    print("%d不是素数"%num)

'''
找出从1-100间的素数
'''
import math
for num in range(2,100):
    is_prime = True
    for factor in range(2,int(math.sqrt(num))+1):
        if num%factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
