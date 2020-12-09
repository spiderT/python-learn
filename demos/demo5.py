dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # 输出键为'one' 的值  #This is one
print(dict[2])  # 输出键为 2 的值  #This is two
print(tinydict)  # 输出完整的字典  #{'name': 'runoob', 'code': 6734, 'dept': 'sales'}
print(tinydict.keys())  # 输出所有键  #dict_keys(['name', 'code', 'dept'])
print(tinydict.values())  # 输出所有值  #dict_values(['runoob', 6734, 'sales'])
