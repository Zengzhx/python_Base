class Student(object):
    pass


s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性 (只能绑定一个实例)
print(s.name)


def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)  # 动态给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age)


#但是，给一个实例绑定的方法，对另一个实例是不起作用的：
# s2 = Student() # 创建新的实例
# s2.set_age(25) # 尝试调用方法


# 动态给class 绑定一个属性
def set_score(self, score):
    self.score = score
Student.set_score = set_score

ss1 = Student()
ss1.set_score(100)
print(ss1.score)

ss2 = Student()
ss2.set_score(10)
print(ss2.score)

'''
使用__slots__

但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
'''
# class Student(object):
#     __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

# s = Student() # 创建新的实例
# s.name = 'Michael' # 绑定属性'name'
# s.age = 25 # 绑定属性'age'
# s.score = 99 # 绑定属性'score'
#
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
#

