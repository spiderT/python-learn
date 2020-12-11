# # 定义函数
# def printme(str):
#     print(str)
#     return

# # 调用函数
# printme("我要调用用户自定义函数!")
# printme("再次调用同一函数")

# # python 传不可变对象实例
# def ChangeInt(a):
#     a = 10

# b = 2
# ChangeInt(b)
# print(b)  # 结果是 2
# # 实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象，在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它。

# # 传可变对象实例
# # 可写函数说明
# def changeme(mylist):
#     "修改传入的列表"
#     mylist.append([1, 2, 3, 4])
#     print("函数内取值: ", mylist) # 函数内取值:  [10, 20, 30, [1, 2, 3, 4]]
#     return

# # 调用changeme函数
# mylist = [10, 20, 30]
# changeme(mylist)
# print("函数外取值: ", mylist) # 函数外取值:  [10, 20, 30, [1, 2, 3, 4]]
# # 实例中传入函数的和在末尾添加新内容的对象用的是同一个引用

# # 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
# def printinfo(name, age):
#     "打印任何传入的字符串"
#     print("Name:", name)
#     print("Age:", age)
#     return

# #调用printinfo函数
# printinfo(age=50, name="miki")  # Name: miki  Age: 50

# # 调用函数时，默认参数的值如果没有传入，则被认为是默认值。
# def printinfo(name, age=35):
#     print("Name:", name, "Age:", age)
#     return

# #调用printinfo函数
# printinfo(age=50, name="miki") # Name: miki Age: 50
# printinfo(name="miki")         # Name: miki Age: 35

# # 一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数,声明时不会命名。
# # 加了星号（*）的变量名会存放所有未命名的变量参数。
# def printinfo(arg1, *vartuple):
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return

# # 调用printinfo 函数
# printinfo(10)  # 10
# printinfo(70, 60, 50)  # 70 60 50

# # 匿名函数
# sum = lambda arg1, arg2: arg1 + arg2

# # 调用sum函数
# print(sum(10, 20)) # 30
# print(sum(20, 20)) # 40

total = 0  # 这是一个全局变量


def sum(arg1, arg2):
    #返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)  # 30
    return total


#调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)  # 0
