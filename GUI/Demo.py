from tkinter import *

class GUI(Frame):
    i = 0

    def hello(self):
        print('hello')

    def about(self):
        if self.i<1:
            label = Label(root, text='Zengzhx', fg='red', bg='blue')
            label.pack(expand=YES, fill=BOTH)
            self.i += 1


root = Tk()
gui  = GUI()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='打开', command=gui.hello())
filemenu.add_command(label='保存')
filemenu.add_separator()
filemenu.add_command(label='退出', command=root.quit)
menubar.add_cascade(label='文件', menu=filemenu)

# helpmenu = Menu(menubar, tearoff=0)
# helpmenu.add_command(label='关于作者', command=gui.about())
# menubar.add_cascade(label='关于', menu=helpmenu)

root.config(menu=menubar)
root.geometry('300x400')
root.mainloop()