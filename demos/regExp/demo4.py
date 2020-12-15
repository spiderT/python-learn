import re
pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
print(m) # None
m = pattern.match('one12twothree34four', 2, 10)  # 从'e'的位置开始匹配，没有匹配
print(m) # None

m = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配
print(m)  # 返回一个 Match 对象 <re.Match object; span=(3, 5), match='12'>
m.group(0)  # 可省略 0
m.start(0)  # 可省略 0
m.end(0)  # 可省略 0
m.span(0)  # 可省略 0
