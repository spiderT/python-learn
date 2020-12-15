import re

# result1 = re.findall(r'\d+', 'baidu 123 google 456')

# pattern = re.compile(r'\d+')  # 查找数字
# result2 = pattern.findall('baidu 123 google 456')
# result3 = pattern.findall('bai88du123google456', 0, 10)

# print(result1) # ['123', '456']
# print(result2) # ['123', '456']
# print(result3) # ['88', '123']

it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())
# 12
# 32
# 43
# 3
