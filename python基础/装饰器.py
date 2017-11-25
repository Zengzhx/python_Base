#
#
#现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，
#

import functools
#日志功能
# def log(func):
#     def wrapper(*args, **kw):
#         print('function %s() ' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，
# 写出来会更复杂。比如，要自定义log的文本：
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log('execute')
# def now():
#
#     print('2017-08-03', now.__name__)
#
# now()


def begin_end():
    def decoretor(funcc):
        def wrapper(*args, **ky):
            print("begin")
            fun = funcc(*args, **ky)
            print("end")
            return  fun
        return wrapper

    return decoretor



@begin_end()
def function():
    print("function")

function()


# def out():
#     def inner():
#         print("inner")
#     return inner
#
# print(out())

if __name__ == '__main__':
    pass
