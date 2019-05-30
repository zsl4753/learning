#正则表达式定义了字符串的匹配
''''''
'''
.               匹配任意字符                           b.t             可以匹配bat/but/b#t/b1t等等
\w              匹配字母/数字/下划线                   b\wt            可以匹配bat/but/b1t/b_t/但不能匹配b#t
\s              匹配空白字符（包括\r\n\t)              love\syou       可以匹配love you
\d              匹配数字                              \d\d             可以匹配01/23/99
\b              匹配单词边界                          \bthe\b          匹配the这个单词
^               匹配字符串的开始                       ^The            匹配The开头的字符串
$               匹配字符串的结尾                       .exe$           匹配.exe结尾的字符串
\W              匹配非字母/数字/下划线                 b\Wt            可以匹配b#t\b@t但不能匹配bat
\S              匹配非空白字符                        love\Syou        匹配love@you等，但不能匹配love you
\D              匹配非数字                            \d\D             匹配9a/3#
\B              匹配非单词边界                        \Bio\B           匹配非io为开头或结尾的单词
[]              匹配来自字符集的任意单一字符           [aeiou]          匹配任一元音字母
[^]             匹配不在字符集中的任意单一字符         [^aeiou]          匹配任一非元音字符

*               匹配0次或多次
+               匹配1次或多次
？               匹配0次或1次
{N}             匹配N次
{M,}            匹配至少M次
{M,N}           匹配至少M次至多N次
|               分支
(?#)            注释
(exp)           匹配exp并捕获到自动命名的组中
(?<name>exp)    匹配exp并捕获到命名为name的组中
(?:exp)         匹配exp但是不捕获匹配的文本
(?=exp)         匹配exp前面的位置             \b\w+(?=ing)        匹配i'm dancing中的danc
(?<=exp)        匹配exp后面的位置             (?<=\bdanc)\w+\b     匹配i love dancing 中的ing
(?!exp)         撇配后面不是exp的位置
(?<!=exp)       匹配前面不是exp的位置            
*?              重复任意次，但尽可能少重复
+?              重复1次或多次，但尽可能少重复
??              重复0次或1次，但尽可能少重复
{M,N}?          重复M到N次，但尽可能少重复
{M,}?           重复M次以上，但尽可能少重复

'''

'''
python对正则表达式的支持（re模块）
    compile(pattern, flags = 0)                     编译正则表达式返回正则表达式对象
    match(pattern,string,flags =0)                  用正则表达式匹配字符串，成功返回匹配对象，否则返回None
    search(pattern,string,flags=0)                  搜索字符串中第一次出现正则表达式的模式，返回值同上
    spilt(pattern,string,maxspilt=0,flags =0)       用正则表达式指定的模式分隔符拆分字符串，返回列表
    sub（pattern,repl,string,count=0,flags =0)      用指定的字符串替换源字符串的中与正则表达式匹配的模式，可以指定替换次数
    fullmatch(pattern,string,flags=0)               match函数的完全匹配（从字符串开头到结尾）版本
    findall(pattern,string,flags=0)                 查找字符串所有与正则表达式匹配的模式，返回字符串的列表
    finditer(pattern,string,flags=0)                查找字符串所有与正则表达式匹配的模式，返回一个迭代器
    group（）                                        在正则表达式中用于获取分段截获的字符串
    purge()                                         消除隐式编译的正则表达式的缓存
    re.I/re.IGNORECASE                              忽略大小写
    re.M/re.MULTILINE                               多行匹配标记
    
    说明：上面提到的说法，实际开发中也可以用正则表达式对象的方法来替代，如果一个正则表达式要反复的使用，那么先通过compile函数编译正则表达式，并创建出
          正则表达式对象更明智.flags 是模式设计 如re.I等等
'''
import re
def example1():
    '''
    验证输入用户名和qq号是否有效并给出对应的提示信息。
    要求：用户名必须由数字、字母或下划线构成且长度在6~20个字符之间，qq必须是5~12的数字且首位不能为0
    '''

    username = input('请输入用户名:')
    qq = input('请输入qq号:')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)#第一个参数是正则表达式字符串或正则表达式对象，第二个参数是要做匹配的字符串对象
    if not m1:
        print("请输入有效的字符串")
    m2 = re.match(r'^[1-9][0-9]{4,11}$',qq)
    if not m2:
        print("请输入有效qq号")
    if m1 and m2:
        print("你的信息是有效的")
    '''
    注意：字符串前面加上了r，即原始字符串的写法
    '''

def example2():
    '''
    从一段文字中提取出国内手机号码
    电信号段：133/153/180/181/189/177
    联通号段：130/131/132/155/156/185/186/145/176
    移动号段：134/135/136/137/38/139/150/151/152/157/158/159/182/188/147/178
    '''
    #创建正则表达式对象，使用了前瞻和后顾保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    pattern1 = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    sentence = '''
        重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
        不是15600998765，也是110或119，王大锤的手机号才是15600998765。
        '''
    mylist = re.findall(pattern,sentence)
    print(mylist)
    print('------------------------分割性----------------------')
    #通过迭代器取出匹配对象并获得匹配的内容
    for temp in re.finditer(pattern,sentence):
        print(temp.group())
    print('----------------------分割线----------------------')
    #通过search函数指定搜索位置找出所有匹配
    m = re.search(pattern,sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence,m.end())
def example3():
    '''
    替换字符串中的不良内容
    :return: 
    '''
    sentence = '你丫是个傻叉吗？我操你大爷的。FUCK you.'
    purified = re.sub('[艹肏操]|fuck|shit|傻[比逼叉]|煞笔','*',sentence,flags = re.IGNORECASE)
    print(purified)
def example4():
    '''
    拆分长字符串
    :return: 
    '''
    poem = "床前明月光，疑是地上霜，举头望明月，低头思故乡"
    sentence_list = re.split(r'[,.，。]',poem)
    print(sentence_list)
    while '' in sentence_list:
        sentence_list('')
    print(sentence_list)
def string1():
    #转义字符
    print('My brother \'s name is \'007\'')
    #原始字符
    print(r'My brither \'s name is \'007\'')

    str = 'hello123world'
string1()


