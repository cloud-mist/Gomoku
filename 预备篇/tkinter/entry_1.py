#单行文本输入小部件

import tkinter as tk

class EntryApp(tk.Tk):
	def __init__(self):
		super().__init__()
		self.entry = tk.Entry()
		self.entry.pack()

if __name__ == '__main__':
	app = EntryApp()
	app.mainloop()

