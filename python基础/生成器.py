#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：

'''
generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：
'''


'''
如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：

最难理解的就是generator和函数的执行流程不一样。
函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''

it = iter([1, 2, 3, 4, 5])

from math import *

ash=hex(int(sqrt(abs(1))))
print(ash)