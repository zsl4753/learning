'''
输出斐波那契前20个数
'''

a = 0

b = 1

for _ in range(20):

    (a, b) = (b, a + b)

    print(a, end=' ')
'''
def fibo(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    elif x == 0:
        return 0
    else:
        return fibo(x-1)+fibo(x-2)

for i in range(10):
print(fibo(i))
'''
