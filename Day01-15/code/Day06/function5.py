"""
函数的参数
- 位置参数
- 可变参数
- 关键字参数
- 命名关键字参数

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""


# 参数默认值
def f1(a, b=5, c=10):
    return a + b * 2 + c * 3


print(f1(1, 2, 3))
print(f1(100, 200))
print(f1(100))
print(f1(c=2, b=3, a=1))  # 参数顺序调整！！


# 可变参数
def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(f2(1, 2, 3))
print(f2(1, 2, 3, 4, 5))
print(f2())

""" 多行注释
python的函数中会出现*args和**kwargs两个形参，其作用分别为
*args：接收若干个位置参数，转换成元组tuple形式
**kwargs：接受若干个关键字参数，转换成字典dict( key:value )形式
args和kwargs只是python的约定，命名成任何名字都行，但这两个是python的标准用法。
"""

# 关键字参数
def f3(**kw):
    if 'name' in kw:
        print('欢迎你%s!' % kw['name'])
    elif 'tel' in kw:
        print('你的联系电话是: %s!' % kw['tel'])
    else:
        print('没找到你的个人信息!')


param = {'name': '骆昊', 'age': 38}
f3(**param)
f3(name='骆昊', age=38, tel='13866778899')
f3(user='骆昊', age=38, tel='13866778899')
f3(user='骆昊', age=38, mobile='13866778899')
