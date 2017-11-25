

def a_fun(a, b):
    return a, b

a, b = a_fun('bbb','aaaa')
print(a, b)

print(a_fun('bbb','aaaa'))


#a2 + b2 + c2 + ……。

#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
# 但是，调用该函数时，可以传入任意个参数，包括0个参数：
#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
def add_function(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print(sum)

add_function(2)


#关键字参数
#键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('aaa',111)

person('Bob', 35, gender='M', job='Engineer')


#参数组合
#请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数 和 关键字参数。

#小结
#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。