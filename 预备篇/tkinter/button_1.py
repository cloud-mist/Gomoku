#最基础的按钮
import tkinter as tk

class ButtonApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.image = tk.PhotoImage(file='z.png')
        self.btn = tk.Button(text='first button ',
                             image = self.image, 
                             compound = tk.BOTTOM,
                             command = self.disable_btn,    #按钮绑定的函数
                             )
        #实例化Button类,text为按钮添加文字,image 加图片. compound，如果不加，只显示图片，将图片放置右边
        self.btn.pack(
            padx = 10,
            pady = 20,
            expand = True,
            fill = tk.BOTH,
        )             # 将实例化的小部件打包到其父部件中，若没有这行，按钮不会显示
    def disable_btn(self):
        self.btn.config(state=tk.DISABLED)
"""
用来控制按钮的位置和排列。pack()方法支持很多属性的设置 
    before：在打包某一个小部件之前打包；
    expand：如果父级部件增大，也随之增大；
    fill：如果小部件增大则填充小部件；
    ipadx：在X轴方向上填充内边距；
    ipady：在Y轴方向上填充内边距；
    padx：在X轴方向填充；
    pady:在Y轴方向填充；
    side:在指定位置添加小部件；
"""
    #禁用按钮


if __name__ == '__main__': 
    app = ButtonApp()
    app.mainloop()