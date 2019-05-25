'''
题目：计算两个正整数的最大公约数和最小公倍数
算法：最小公倍数是两个数相乘除以最大公约数
'''
x = int(input('x='))
y = int(input('y='))
if x>y:
    x,y = y,x
for factor in range(x,0,-1):
    if x%factor == 0 and y%factor == 0:
        print('%d和%d的最大公约数是%d'%(x,y,factor))
        print("%d和%d的最小公倍数是%d"%(x,y,x*y//factor))
        break
