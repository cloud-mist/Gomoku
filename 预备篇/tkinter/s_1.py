import tkinter as tk    #导入包并别名为tk

def win():
    print("这是个字符串")

'''主窗口'''
root = tk.Tk()          #实例化一个Tk主窗口，赋给root
root.title("my first window")      #设置窗口标题title

"""按钮部件"""
btn = tk.Button(root, text='点我吧')    #实例化一个按钮类
btn.pack(padx=200, pady=50)             #设置按钮大小
btn.config(command=win)                 #点按钮在控制台调用win

root.mainloop()         #使得窗口运行