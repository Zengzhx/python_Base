class Student(object):

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        self._age = value

s = Student()
s.age = 11
print(s.age)
#
# 将对象的 get set 方法设置成为 属性输出

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        area = self._width * self._height
        return area

sc = Screen()
sc.width  = 30
sc.height = 40
print(sc.resolution)
