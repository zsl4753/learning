import tkinter

flag = True
def mouse_evt_handle(evt = None):
    global  flag
    row = round((evt.y-20)/40)#round() 方法返回浮点数x的四舍五入值
    col = round((evt.x-20)/40)
    pos_x = 40*col
    pos_y = 40*row
    if flag == True:
        canvas.create_oval(pos_x,pos_y,pos_x+40,40+pos_y,fill = 'black')
    else:
        canvas.create_oval(pos_x, pos_y, pos_x + 40, 40 + pos_y, fill='white')
    flag = ~flag
top = tkinter.Tk()
top.geometry("620x620")
top.title("五子棋")
top.resizable(0,0)
top.wm_attributes('-topmost',1)#设置窗口指定
#画布

canvas = tkinter.Canvas(top,width = 600,height = 600,bd = 0,highlightthickness = 0)
canvas.bind('<Button-1>',mouse_evt_handle)
canvas.create_rectangle(0,0,600,600,fill = 'yellow',outline = 'white')
for index in range(15):
    canvas.create_line(20,20+40*index,580,20+40*index,fill ='black')
    canvas.create_line(20+40*index,20,20+40*index,580,fill = 'black')
canvas.create_rectangle(15,15,585,585,outline = 'black',width = 4)
canvas.pack()
canvas.mainloop()

