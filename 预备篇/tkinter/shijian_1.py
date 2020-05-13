import tkinter as tk

class ButtonApp(tk.Tk):
    """每点击一次按钮，都会在控制台打印一次，用command命令来绑定"""
    def __init__(self):
        super().__init__()
        self.title("按钮事件")
        self.btn = tk.Button(text="按钮", command = self.print_button)
        self.btn.pack()
    
    def print_button(self):
        print("点击了按钮")

if __name__ == "__main__":
    app = ButtonApp()
    app.mainloop()