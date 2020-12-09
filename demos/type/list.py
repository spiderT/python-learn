# # 更新列表
# list = []  # 空列表
# list.append('Google')  # 使用 append() 添加元素
# list.append('Runoob')
# print(list) # ['Google', 'Runoob']

# # 删除列表元素
# list1 = ['physics', 'chemistry', 1997, 2000]

# del list1[2]
# print(list1) # ['physics', 'chemistry', 2000]

# list.count(obj)
# 统计某个元素在列表中出现的次数
# list = ['physics', 'abc', 'chemistry', 1997, 2000, 'abc']
# print(list.count('abc'))  # 2

# # list.extend(seq)
# # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# list1 = [1, 2]
# list2 = [3, 4, 5]
# list1.extend(list2)
# print(list1) # [1, 2, 3, 4, 5]

# list.index(obj)
# 从列表中找出某个值第一个匹配项的索引位置
# list = ['physics', 'abc', 'chemistry', 1997, 2000, 'abc']
# print(list.index('abc')) # 1

# # list.insert(index, obj)
# # 将对象插入列表
# list1 = [1, 2]
# list2 = [3, 4, 5]
# list1.insert(0, list2)
# print(list1)  # [[3, 4, 5], 1, 2]

# list.pop([index=-1])
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# list = ['physics', 'abc', 'chemistry', 1997, 2000, 'abc']
# print(list.pop()) # abc
# print(list.pop(2)) # chemistry

# # list.remove(obj)
# # 移除列表中某个值的第一个匹配项
# list = ['physics', 'abc', 'chemistry', 1997, 2000, 'abc']
# list.remove('abc')
# print(list) # ['physics', 'chemistry', 1997, 2000, 'abc']


# # list.reverse()
# # 反向列表中元素
# list = ['physics', 'abc', 'chemistry', 1997, 2000, 'abc']
# list.reverse()
# print(list) # ['abc', 2000, 1997, 'chemistry', 'abc', 'physics']

# # list.sort(cmp=None, key=None, reverse=False)
# # 对原列表进行排序
# list = [9999, 1, 11111, 1997, 2000, 11]
# list.sort()
# print(list) # [1, 11, 1997, 2000, 9999, 11111]




# # cmp(list1, list2)
# # 比较两个列表的元素
# # python 3.4.3 的版本中已经没有cmp函数，被operator模块代替，在交互模式下使用时，需要导入模块。
# import operator              #首先要导入运算符模块
# print(operator.gt(1,2))  # False    #意思是greater than（大于）
# print(operator.ge(1,2))  # False    #意思是greater and equal（大于等于）
# print(operator.eq(1,2))  # False    #意思是equal（等于）
# print(operator.le(1,2))  # True     #意思是less and equal（小于等于）
# print(operator.lt(1,2))  # True     #意思是less than（小于）



# # len(list) 列表元素个数
# # max(list) 返回列表元素最大值
# # min(list) 返回列表元素最小值
# list = [9999, 1, 11111, 1997, 2000, 11]
# print(len(list)) # 6
# print(max(list)) # 11111
# print(min(list)) # 1


# list(seq)
# 将元组转换为列表
a = (1,2,3)
print(list(a))  # [1, 2, 3]

