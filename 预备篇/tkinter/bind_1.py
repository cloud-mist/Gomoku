#bind 方法用于在小部件上绑定一个事件到一个函数上
"""
bind()方法在部件类中进行定义，并且其接受三个参数：
    sequence：事件的组合序列，用来修饰事件；
    func：回调函数；
    add：可选的参数，用于指定回调函数额外调用到另一个函数还是替换上一个函数
"""
import tkinter as tk
class EventApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("事件之bind")
        self.btn = tk.Button(text="按钮",height=5, width=10)
        self.frm = tk.Frame(bg="green", height=100, width=100)

        self.frm.bind("<Enter>", self.print_mouse_status)   #鼠标进入小部件事件
        self.frm.bind("<Leave>", self.print_mouse_status)   #鼠标离开小部件事件
        self.frm.bind("<B1-Motion>", self.print_mouse_status)   #鼠标点击拖动小部件事件
        self.btn.bind("<Button>", self.mouse_click)

        self.frm.pack(padx=20,pady=20)
        self.btn.pack(padx=20,pady=20)

    def print_mouse_status(self,event):
        print("鼠标状态： ", event.type)
        print("鼠标位置： ", event.x, event.y)
    
    def mouse_click(self,event):
        key ={1:"左键", 2:"滚轮", 3:"右键"}
        print(event.type,"单击了鼠标{}".format(key[event.num]))

if __name__ == "__main__":
    app = EventApp()
    app.mainloop()