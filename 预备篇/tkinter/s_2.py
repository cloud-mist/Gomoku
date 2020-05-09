#对第一个例子的模块化
import  tkinter as tk

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("第一个程序升级版")
        self.ini_ui()

    def ini_ui(self):
        self.btn = tk.Button(self, text='点我吧')
        self.btn.pack(padx=200,pady=30)
        self.btn.config(command=self.tell_u)
    
    def tell_u(self):
        print("这是个字符串")
    
if __name__ == '__main__':
    app = Main()
    app.mainloop()