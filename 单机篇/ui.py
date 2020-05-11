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
    cvs_1.create_line(30, 30*i, 450, 30*i)
    cvs_1.create_line(30*i, 30, 30*i, 450)
# 棋盘的五个点
point_x = [3, 3, 11, 11, 7]
point_y = [3, 11, 3, 11, 7]
for i in range(5):
    cvs_1.create_oval(30 * point_x[i] + 27, 30 * point_y[i] + 27, 
                       30 * point_x[i] + 33, 30 * point_y[i] + 33, fill = "black")

window.mainloop()