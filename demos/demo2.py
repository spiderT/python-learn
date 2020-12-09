# [头下标:尾下标] 获取的子字符串包含头下标的字符，但不包含尾下标的字符。
# s = 'abcdef'
# a = s[1:5]
# print(a)  #'bcde'





# 加号（+）是字符串连接运算符，星号（*）是重复操作。
str = 'Hello World!'
 
# print(str)           # 输出完整字符串 Hello World!
# print(str[0])        # 输出字符串中的第一个字符 H
# print(str[2:5])      # 输出字符串中第三个至第六个之间的字符串 llo
# print(str[2:])       # 输出从第三个字符开始的字符串 llo World!
# print(str * 2)       # 输出字符串两次 Hello World!Hello World!
# print(str + "TEST")  # 输出连接的字符串 Hello World!TEST


# 第三个参数，参数作用是截取的步长
print(str[2:5:2])      # lo


