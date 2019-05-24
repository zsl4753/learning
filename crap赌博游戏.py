'''
玩家掷两个骰子，每个骰子点数为1-6，如果第一次点数和为7或11，则玩家胜；
如果点数和为2、3或12，则玩家输庄家胜。
若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，
直至点数和等于第一次掷出的点数和则玩家胜；
若掷出的点数和为7则庄家胜。
'''

import random
def crap():
    '''
    
    :return: 1:玩家赢
              0：庄家赢
    '''
    s1 = [1,2,3,4,5,6]
    x1 = random.choice(s1)
    x2 = random.choice(s1)
    sum1 = x1 + x2
    if sum1 == 7 or sum1 == 11:
        print("玩家赢，掷出了%d和%d两个数，总和是%d"%(x1,x2,sum1))
    elif sum1 == 2 or sum1 == 3 or sum1 == 12:
        print("庄家赢，掷出了%d和%d两个数，总和是%d" % (x1, x2, sum1))
    else:
        print("第一次掷出了%d和%d两个数，总和是%d，不满足胜利要求，所以重新掷"%(x1,x2,sum1))
        sum2 = 0
        n = 0
        while(sum2 != 7 and sum2 != sum1):
            x1 = random.choice(s1)
            x2 = random.choice(s1)
            sum2 = x1+x2
            n = n+1
        if sum2 == 7:
            print("庄家赢，在第%d次掷出了%d和%d两个数，总和是%d" % (n,x1, x2, sum2))
        else:
            print("玩家赢，在第%d次掷出了%d和%d两个数，总和是%d" % (n, x1, x2, sum2))


crap()
