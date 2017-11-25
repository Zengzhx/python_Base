
L = [
    ['Apple', 'Alibaba', 'Huawei', 'Baidu','Google'],
    ['Java', 'C', 'C++', 'Python'],
    ['a', 'b', 'c']
]
#
#
# ii = 0
# for i in L:
#     jj = 0
#     for j in i:
#         if j.__eq__('Python'):
#             print(ii, jj, end='')
#         jj += 1
#     ii += 1
#
#
# #Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)
# enumerate()
# for i,i_value in enumerate(L):
#     for j,j_value in enumerate(i_value):
#         print(i,j,j_value)

print([x * x for x in range(1, 11)])

#还可以使用两层循环，可以生成全排列：
print([m + n for m in 'ABC' for n in 'XYZ'])

# import os
# print([d for d in os.listdir('.')])


#dict 字典 迭代 items()
d = {'x': 'A', 'y': 'B', 'z': 'C' }

for k, v in d.items():
    print(k,end='=v',)
