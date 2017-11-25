#filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
#filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

#
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
# for a in _odd_iter():
#     print(a)


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
v = sorted(L)
print(v)