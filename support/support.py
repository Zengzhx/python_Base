def print_func( par ):
    print ("Hello : ", par)
    return


def fib(n):
    a , b = 0 , 1
    while b<n:
        print( b,end='' )
        a,b=b,a+b
        print()


def fiba(n):
    a , b = 0 , 1
    result = []
    while b<n:
        result.append(b)
        a , b=b,a+b
    print(result)


'''
__name__属性
一个模块被另一个程序第一次引入时，其主程序将运行。
如果我们想在模块被引入时，模块中的某一程序块不执行，
我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
'''
def mode():
    if __name__ == '__main__':
        print(__name__)
    else:
        print(__name__)
mode()
'''
说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
'''