for x in range(0,21):#公鸡最多20只
    for y in range(0,35):#母鸡最多34只
        z = 100 - x - y
        if 5*x+3*y+z/3 == 100:
            print("方法如下：")
            print('公鸡是',x)
            print('母鸡是',y)
print('雏鸡是',z)
