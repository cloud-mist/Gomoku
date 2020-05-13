import tkinter as tk
window = tk.Tk()
window.title("Gomaku")
cvs_1 = tk.Canvas(window, bg="SandyBrown", width=480, height=480)  # 画布
cvs_2 = tk.Canvas(window, width = 200, height = 50,bg="black")
btn_1 = tk.Button(cvs_2,text="START",font=('黑体', 10),fg='blue',width=10,height=2)
btn_2 = tk.Button(cvs_2,text="REDO", font=('黑体', 10),fg='blue',width=10,height=2)
btn_3 = tk.Button(cvs_2,text="CTRLz",font=('黑体', 10),fg='red', width=10,height=2)
# 使用gird布局管理器好些，灵活
cvs_1.grid(row=0,column=0)      
cvs_2.grid(row=0,column=1)
btn_1.grid(row=0,column=0)
btn_2.grid(row=1,column=0)
btn_3.grid(row=2,column=0)
# 棋盘划线
for i in range(1,16):
    cvs_1.create_line(30, 30*i, 450, 30*i)  #参数 起点x,y 终点x,y
    cvs_1.create_line(30*i, 30, 30*i, 450)
# 棋盘的五个点绘制  #oval参数，定义对角线的两个点的x,y
point_x = [3, 3, 11, 11, 7]
point_y = [3, 11, 3, 11, 7]
for i in range(5):
    cvs_1.create_oval(30 * point_x[i] + 26.5, 30 * point_y[i] + 26.5, 
                      30 * point_x[i] + 33.5, 30 * point_y[i] + 33.5, fill = "black")  

#参数
r = 10
click_x = 0
click_y = 0
piece_flag = 1     #棋子标志，1为白，-1为黑
piece_color = "black"  #当前棋子颜色
all_black = []      #黑子坐标存储
all_white = []      #白子坐标存储
all_pieces =[]      #所有棋子坐标存储
end_flag = 0        #结束标志

def mouse_back(event):
    global click_x, click_y
    click_x = event.x
    click_y = event.y
    mouse_judge()

cvs_1.bind("<Button-1>", mouse_back)


def mouse_judge():
    global click_x, click_y, piece_flag, all_pieces
    #将棋子（黑白）坐标全部存进去
    all_pieces = all_black + all_white   
    i = 0
    j = 0
    #确定鼠标点击位置所在的格子
    while click_x > (30 + 15 * i):     
        i += 1
    while click_y > (30 + 15 * j):
        j += 1
    # 将一个格子分成四个区域，根据鼠标点击位置所在区域分得格子的顶点
    if(i%2==1):            
        click_x = 30 + 15 * (i - 1)
    else:
        click_x = 30 + 15 * i 
    if(j%2==1): 
        click_y = 30 + 15 * (j - 1)
    else:
        click_y = 30 + 15 * j

    if piece_flag == 1:
        put_piece("black")
    elif piece_flag == -1:
        put_piece("white")

def put_piece(piece_color):
    """落子"""
    global piece_flag
    # 只能在棋谱内产生棋子
    if (click_x>=30)and(click_x<=450)and(click_y>=30)and(click_y<=450):
        # 一个点只能产生一个棋子 
        if (click_x, click_y) not in all_pieces:  
            
            if end_flag == 0:
                cvs_1.create_oval(click_x - r, click_y - r,
                                  click_x + r, click_y + r, 
                                  fill = piece_color)
                piece_flag *= -1
                #把坐标添加到坐标列表中
                if piece_color == "white":
                    all_white.append((click_x, click_y))
                else:
                    all_black.append((click_x, click_y))
                  













window.mainloop()