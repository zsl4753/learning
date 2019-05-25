'''
打印三角图形
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
'''

row = int(input('row = '))
#右三角
for i in range(row):
    for _ in range(i+1):
        #print函数不会在字符串末尾添加一个换行符，而是添加一个空字符串，
        # 其实这也是一个语法要求，表示这个语句没结束。
        print('*',end ='')
    print()

#左三角
for i in range(row):
    for j in range(row):
        if j <row - i - 1:
            print(' ',end = '')
        else:
            print('*',end = '')
    print()

#中三角
for i in range(row):
    for _ in range(row - i- 1):
        print(' ',end ='')
    for _ in range(2*i+1):
        print('*',end ='')
    print()
