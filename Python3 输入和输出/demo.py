'''
输出格式美化
Python两种输出值的方式: 表达式语句和 print() 函数。
第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
'''

s = 'Hello World'
print(str(s))
print(repr(s))


x = 10 * 3.25
y = 200 * 200
s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) ;
print(s)

#  repr() 函数可以转义字符串中的特殊字符
hello = 'hello, runoob\n'
hello_repr = repr(hello)
print(hello_repr)
hello_str = str(hello)
print(hello_str)


for x in range(1,11):
    #print(repr(x).rjust(2),repr(x**2).rjust(4),repr(x**3).rjust(4))
    print('{0:2d},{1:2d},{2:2d}'.format(x,x**2,x**3))


'''
str.format() 的基本使用如下:
'''
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))

'''
位置及关键字参数可以任意的结合:
#{0} 代表位置     #{aaa} 可以指定参数
'''
print('站点列表 {0}, {1}, 和 {aaa}。'.format('Google', 'Runoob', aaa='Taobao'))




'''
'!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
'''
import  math
print('常量 PI 的值近似为： {!r}。'.format(math.pi))


'''
可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
'''

print('常量 PI 的值近似为： {:.3f}。'.format(math.pi))


'''
如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 :
'''

table = {'taobao': 1 , 'google': 2 , 'jd': 3}
print('taobao: {0[taobao]:d} ; google: {0[google]:d}  ; jd: {0[jd]:d}'.format(table))

# table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))




'''1
读取键盘输入
Python提供了 input() 置函数从标准输入读入一行文本，默认的标准输入是键盘。
input 可以接收一个Python表达式作为输入，并将运算结果返回。
'''
# str = input('请输入：')
# print(str)


'''
读和写文件
open() 将会返回一个 file 对象，基本语法格式如下:
    open(filename, mode)
filename：filename 变量是一个包含了你要访问的文件名称的字符串值。
mode：mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
'''

wfile = open("C:\\Users\\75\\Desktop\\aaa\\python_demo.txt")
local = wfile.tell()
print(local)



'''
f.seek()
如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符
'''





'''
pickle 模块
python的pickle模块实现了基本的数据序列和反序列化。
通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
'''
import pickle
# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
#序列化
output = open('C:\\Users\\75\\Desktop\\aaa\\data.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1,output)
output.close()

#反序列化
data = open('C:\\Users\\75\\Desktop\\aaa\\data.pkl','rb')
x = pickle.load(data);
data.close()
print(x)


'''
File(文件) 方法
'''
output = open('C:\\Users\\75\\Desktop\\aaa\\aaa.txt', 'wb')
print ("文件名为: ", output.name)
fid = output.fileno()
print ("文件描述符为: ", fid)
output.close()


'''
捕捉异常
:except
'''
while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again   ")

'''
try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。
这个子句将在try子句没有发生任何异常的时候执行。例如:
'''


'''
抛出异常
Python 使用 raise 语句抛出一个指定的异常。例如:
'''
raise NameError('HiThere')


'''
预定义的清理行为
'''
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")


