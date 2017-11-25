"""
Python 引用其他.py文件中的类和类的方法
#HelloWorld是文件名称，Hello是类
from HelloWorld import Hello
"""

# from DemoClass import  MyClass
#
# x = MyClass(10,20)
#
# print(x.i)
# print(x.r)

# x.f()

# from people import people
#
# x = people('zhangsan','man',20)
#
# x.speak()

from people import people,student,school,JustCounter

# peo =people('people','man',14)
# peo.over()
#
# stu = student('lisi','man',13,'高三','一中')
# stu.over()


just = JustCounter()

just.count()
just.count()

print(just.publicCount)
print(just._JustCounter__secretCount)#私有属性访问

