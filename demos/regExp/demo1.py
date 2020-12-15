import re
# print(re.match('www', 'www.baidu.com').span())  # 在起始位置匹配    (0, 3)
# print(re.match('com', 'www.baidu.com'))  # 不在起始位置匹配          None

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group()) # Cats are smarter than dogs
    print("matchObj.group(1) : ", matchObj.group(1)) # Cats
    print("matchObj.group(2) : ", matchObj.group(2)) # smarter
else:
    print("No match!!")
