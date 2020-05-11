import tkinter as tk    
# Scale()是另一个显示形式的选值小部件，
# 默认选值范围0到100，对齐方式为水平对齐.
# 是滑块的形式
class SelectApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.wm_title('first scale window')
        self.select_num1 = tk.Scale()
        self.select_num1.pack()
        self.select_num2 = tk.Scale(from_=1,to=8,orient=tk.HORIZONTAL)
        #指定范围为1到8，并且修改对齐方式为垂直
        self.select_num2.pack()

if __name__ == '__main__':
    app = SelectApp()
    app.mainloop()