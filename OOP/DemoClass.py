class MyClass:
    # 构造方法  只能定  # def __init__(self):
    #     print("默认构造方法")

    # self代表类的实例，而非类
    # 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是
    # self。

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


    def f(self):
        return  print(self.r*self.i)


