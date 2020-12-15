# num = 1

# def fun1():
#     global num  # 需要使用 global 关键字声明
#     print(num) # 1
#     num = 123
#     print(num) # 123

# fun1()
# print(num) # 123


def outer():
    num = 10

    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 100
        print(num) # 100

    inner()
    print(num) # 100


outer()