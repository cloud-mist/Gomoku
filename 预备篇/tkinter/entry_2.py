#创建一个简单的登录窗口界面
import tkinter as tk

class EntryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("输入框按钮程序")
        self.entry1 = tk.Entry()
        self.entry2 = tk.Entry(show="*")    #1.show  隐藏输入信息，
        self.btn1 = tk.Button(text="提交", command=self.get_entry_value)
        self.btn2 = tk.Button(text="重置", command=self.clear_entry_value)
        self.btn3 = tk.Button(text="默认值", command=self.moren_value)

        self.entry1.pack()
        self.entry2.pack()
        self.btn1.pack()
        self.btn2.pack()
        self.btn3.pack()

    def get_entry_value(self):
        """
        2.用 get方法 得到输入的内容，控制台打印内容;
          通过btn1按钮实例，捆绑函数
        """
        e1 = self.entry1.get()    
        e2 = self.entry2.get()
        print("first value: ",e1) 
        print("sec value: ",e2)
    
    def clear_entry_value(self):
        """
        3.用 delete方法 对输入内容删除。
          通过绑定btn2执行
        """
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.entry1.focus_set()    # 对第一个文本输入框设置光标焦点
    def moren_value(self):
        """
        4.输入框直接输入设定的默认值
        """
        self.entry1.insert(0,"cloud_mist")
        self.entry2.insert(0,"123")    

if __name__ == "__main__":
    app = EntryApp()
    app.mainloop()