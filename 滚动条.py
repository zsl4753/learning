import tkinter
from tkinter import ttk
from tkinter import scrolledtext

win = tkinter.Tk()
win.title('Python GUI')
#标签

tkinter.Label(win,text = "Chooes a number:").grid(column = 1,row =0)#列设置为1，行设置为0
tkinter.Label(win,text = 'Enter a name:').grid(column = 0,row =0)#
#按钮点击后调用的函数

def clickMe():
    action.configure(text = 'Hello'+name.get()+' '+numberChosen.get())
    #print('check3 is %s %s'%(type(chvarEn.get(),chvarEn.get())))
#按钮

action = tkinter.Button(win,text = 'Click Me',command = clickMe)
action.grid(column = 2,row = 1)

#文本框
name = tkinter.StringVar()
nameEntered = tkinter.Entry(win,width = 12,textvariable = name)#定义长度为12个字符长度
nameEntered.grid(column = 0,row = 1)
nameEntered.focus()#当程序运行时，光标默认出现再该文本框中

#创建一个下拉列表
number = tkinter.StringVar()
numberChosen = ttk.Combobox(win,width = 12,textvariable = number,state = 'readonly')
numberChosen['values'] = (1,2,3,4,42,100)#设置下拉列表的值
numberChosen.grid(column =1,row =1)
numberChosen.current(0)#设置下拉列表默认显示的值，0表示显示第一位


#复选框
chVarDis = tkinter.IntVar()#用来获取复选框是否被勾选，通过chVarDIs.get()来获取其状态，状态值为Int，勾选为1，反之为0
#text为该复选框后面显示的名称，variable将复选框的状态赋值给一个变量，当state为disabled时，复选框不可选
check1 = tkinter.Checkbutton(win,text = 'Disabled',variable = chVarDis,state = 'disabled')
check1.select()#该复选框是否勾选
check1.grid(column = 0,row = 4,sticky = tkinter.W)#sticky = tkinter.W保证左对齐，参考方向

chvarUn = tkinter.IntVar()
check2 = tkinter.Checkbutton(win,text = 'Unchecked',variable = chvarUn)
check2.deselect()
check2.grid(column = 1,row = 4,sticky = tkinter.W)

charEn = tkinter.IntVar()
check3 = tkinter.Checkbutton(win,text = 'Enabled',variable = charEn)
check3.select()
check3.grid(column = 2,row =4,sticky = tkinter.W)

#单选按钮
#定义几个颜色的全局变量
COLOR1 = "Blue"
COLOR2 = 'Gold'
COLOR3 = "chocolate1"

#单选按钮的回调函数
def radCall():
    radSel = radVar.get()
    if radSel == 1:
        win.configure(background=COLOR1)      # 设置整个界面的背景颜色
    elif radSel == 2:
        win.configure(background=COLOR2)
    elif radSel == 3:
        win.configure(background=COLOR3)


radVar = tkinter.IntVar()#获取单选按钮Value参数对应的值
rad1 = tkinter.Radiobutton(win,text = COLOR1,variable = radVar,value = 1,command = radCall)
rad1.grid(column =0,row =5,sticky = tkinter.W)

rad2 = tkinter.Radiobutton(win,text = COLOR2,variable = radVar,value = 2,command = radCall)
rad2.grid(column = 1,row = 5,sticky = tkinter.W)

rad3 = tkinter.Radiobutton(win,text = COLOR3,variable = radVar,value = 3,command = radCall)
rad3.grid(column = 2,row =5,sticky = tkinter.W)

#滚动文本框
scro1W = 20#设置长度
scro1H = 3#设置高度

scr = scrolledtext.ScrolledText(win,width = scro1W,height = scro1H,wrap = tkinter.WORD)
#wrap = tkinter.WORD  表示在行的末尾如果有一个单词跨行，就放到下一行显示
scr.grid(column =0,columnspan = 3)#将3列合并成一列

win.mainloop()


