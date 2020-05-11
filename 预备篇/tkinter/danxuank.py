import tkinter as tk

class RadioApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('单选框学习')
        self.radio_var = tk.StringVar() #实例化一个tk字符串变量
        self.radio_var.set("woman") #设置变量值
        self.btn_1 = tk.Radiobutton(text='man',value='man',variable=self.radio_var)
        self.btn_2 = tk.Radiobutton(text='woman',value='woman',variable=self.radio_var)
        self.btn_3 = tk.Radiobutton(text='private',value='private',variable=self.radio_var)
        self.btn_4 = tk.Radiobutton(text='a', value='a')

        self.btn_1.pack()
        self.btn_2.pack()
        self.btn_3.pack()
        self.btn_4.pack()

if __name__ == "__main__":
    app = RadioApp()    
    app.mainloop()