import re

# print(re.search('www', 'www.baidu.com').span())  # 在起始位置匹配 (0, 3)
# print(re.search('com', 'www.baidu.com').span())  # 不在起始位置匹配 (10, 13)

line = "Cats are smarter than dogs"

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())  # Cats are smarter than dogs
    print("searchObj.group(1) : ", searchObj.group(1)) # Cats
    print("searchObj.group(2) : ", searchObj.group(2)) # Cats
else:
    print("Nothing found!!")
