import  tkinter as tk

#按钮浮雕类型.在Tkinter中默认可以对按钮设置各种浮雕的样式。其通过Button()类的relief属性来实现
btn_type = [
    {'name':'下沉','relief':tk.SUNKEN},
    {'name':'突出','relief':tk.RAISED},
    {'name':'沟槽','relief':tk.GROOVE},
    {'name': '平的（无边框）', 'relief':tk.FLAT},
    {'name': '实线', 'relief':tk.SOLID}
]

class ButtonApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.img = tk.PhotoImage(file="z.png")
        self.btns = [self.create_btn(r) for r in btn_type]
        for btn in self.btns:
            btn.pack(padx=10, pady=20, side=tk.LEFT)

    def create_btn(self,btn_type):
        return tk.Button(
            text=btn_type["name"],
            image = self.img,
            compound = tk.LEFT,
            relief = btn_type['relief'])

if __name__ == '__main__':
    ui = ButtonApp()
    ui.mainloop()

