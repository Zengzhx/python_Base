from tkinter import *
import tkinter.messagebox as messagebox

#第二步是从Frame派生一个Application类，这是所有Widget的父容器：
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # self.menubutton = Menubutton(self)
        # self.menubutton.pack()
        # self.menu  =Menu(self,text='菜单')
        # self.menu.send(self,self.menubutton)
        self.name1 = Entry(self)
        self.name1.pack()
        self.name2 = Entry(self)
        self.name2.pack()
        self.quitButton1 = Button(self, text='Print', command=self.getValue)
        self.quitButton1.pack()


    def getValue(self):
        print(self.tk_bisque())



app = Application()
# 设置窗口标题:
app.geometry()
app.master.title('Hello World')
# 主消息循环:
app.mainloop()