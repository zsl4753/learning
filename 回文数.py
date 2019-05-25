'''
利用列表进行操作
'''

num = int(input('num : '))
num_str = str(num)
num_list = list(num_str)
num_list_fan = num_list[::-1]
if num_list_fan == num_list:
    print("%d是一个回文数"%num)
else:
    print("%d不是一个回文数"%num)

