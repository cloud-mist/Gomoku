#让用户只能输入数值 选择数值选择框小部件来限制用户输入数值。
#spinbox    scale
#功能一样，但配置和前端显示有差异

import tkinter as tk

class SelectApp(tk.Tk):
    def __init__(self):
        super().__init__()
        #1.self.select_num_1 = tk.Spinbox(from_=0, to=9)
        #实例化，并用from_,to 指定范围
        
        #2.通过value参数指定一个列表作为Spinbox选值框的选值范围
        self.select_num_1 = tk.Spinbox(value=[1,3,5,6,8])
        self.select_num_1.pack()

if __name__ == '__main__':
    app = SelectApp()
    app.mainloop()