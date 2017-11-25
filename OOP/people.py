#父类
class people:

    name = ''

    sex = ''

    __age = 0

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.__age = age

    def speak(self):
        print("name: %s   sex: %s " %(self.name,self.sex))

    def over(self):
        print(self.__class__)


class school:
    school = ''

    def __init__(self, name):
        self.school = name

    def over(self):
        print(self.__class__)

##子类
class student(school,people):

    grade = ''

    def __init__(self, name, sex, age, grade, school_name):
         school.__init__(self, school_name)
         people.__init__(self, name, sex, age)
         self.grade = grade

    def speak(self):
        print("name:%s  sex:%s school:%s grade:%s " % (self.name, self.sex, self.school,  self.grade))

    def over(self):
        print(self.__class__)


"""
类的私有属性

__private_attrs：两个下划线开头，声明该属性为私有，
不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

类的方法

在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。
self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。
类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类地外部调用。self.__private_methods。
"""

class JustCounter:
    __secretCount = 0
    publicCount   = 0


    def count(self):
        self.__secretCount += 1
        self.publicCount   += 1
        print('JustCounter:%s'%(self.__secretCount))


'''
类的专有方法：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 乘方
'''



