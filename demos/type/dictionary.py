# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# print ("dict['Name']: ", dict['Name'])  # dict['Name']:  Zara

# # 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# dict['Age'] = 8 # 更新
# dict['School'] = "RUNOOB" # 添加

# print( "dict['Age']: ", dict['Age'])        # dict['Age']:  8
# print( "dict['School']: ", dict['School'])  # dict['School']:  RUNOOB

# # 能删单一的元素也能清空字典
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# del dict['Name']    # 删除键是'Name'的条目  {'Age': 7, 'Class': 'First'}
# dict.clear()        # 清空字典所有条目       {}
# del dict          # 删除字典                <class 'dict'>

# print (dict)

# # 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
# dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}

# print(dict['Name']) # Manni

# # 键必须不可变，所以可以用数字，字符串或元组充当
# dict = {['Name']: 'Zara', 'Age': 7}

# print (dict['Name']) # TypeError unhashable type: 'list'

# # len(dict) 计算字典元素个数，即键的总数。
# # str(dict) 输出字典可打印的字符串表示。
# # type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型。
# dict = {'Name': 'Zara', 'Age': 7}
# print(len(dict))    # 2
# print(str(dict))    # {'Name': 'Manni', 'Age': 7}
# print(type('Age'))  # <class 'str'>

# # dict.copy() 返回一个字典的浅复制
# dict = {'Name': 'Zara', 'Age': 7}
# dict2 = dict.copy()
# dict2['Name'] = 'Ivy'
# print('dict:', dict, 'dict2:', dict2) # dict: {'Name': 'Zara', 'Age': 7} dict2: {'Name': 'Ivy', 'Age': 7}

# # dict.fromkeys(seq[, val]) 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
# dict = {'Name': 'Zara', 'Age': 7}
# dict2 = dict.fromkeys('a', 'b')
# print(dict2) # {'a': 'b'}

# # dict.get(key, default=None) 返回指定键的值，如果值不在字典中返回default值
# dict = {'Name': 'Zara', 'Age': 7}
# print(dict.get('Name')) # Zara

# # dict.items()  以列表返回可遍历的(键, 值) 元组数组
# dict = {'Name': 'Zara', 'Age': 7}
# print(dict.items()) # dict_items([('Name', 'Zara'), ('Age', 7)])

# # dict.keys()  以列表返回一个字典所有的键
# dict = {'Name': 'Zara', 'Age': 7}
# print(dict.keys()) # dict_keys(['Name', 'Age'])

# # dict.setdefault(key, default=None) 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
# dict = {'Name': 'Zara', 'Age': 7}
# dict.setdefault('aaa', 'ivy')
# print(dict) # {'Name': 'Zara', 'Age': 7, 'aaa': 'ivy'}


# # dict.update(dict2) 把字典dict2的键/值对更新到dict里
# dict = {'Name': 'Zara', 'Age': 7}
# dict2 = {'Age': 17}
# dict.update(dict2)
# print(dict) # {'Name': 'Zara', 'Age': 17}



# # dict.values() 以列表返回字典中的所有值
# dict = {'Name': 'Zara', 'Age': 7}
# print(dict.values()) # dict_values(['Zara', 7])




# # pop(key[,default])  删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
# dict = {'Name': 'Zara', 'Age': 7}
# print(dict.pop('Name'), dict) # Zara  {'Age': 7}


# popitem()  返回并删除字典中的最后一对键和值。
dict = {'Name': 'Zara', 'Age': 7}
print(dict.popitem(), dict) # ('Age', 7)  {'Name': 'Zara'}
