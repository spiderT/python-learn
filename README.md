# python

## 1.基础语法

### 1.1.Python 标识符

所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。  

标识符是区分大小写的。  

以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入。  

以双下划线开头的 __foo 代表类的私有成员.  

以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。  

Python 可以同一行显示多条语句，方法是用分号 ; 分开  

```py
print ('hello');print ('runoob');
```

### 1.2. Python 保留字符

这些保留字不能用作常数或变数，或任何其他标识符名称。  

所有 Python 的关键字只包含小写字母。

![py](images/py1.png)

### 1.3. 行和缩进

Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。  

缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。  

以下实例缩进为四个空格:

```py
if True:
    print ("True")
else:
    print ("False")
```

### 1.4. 多行语句

Python语句中一般以新行作为语句的结束符。  

可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：  

```py
total = item_one + \
        item_two + \
        item_three
```

语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：

```py
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
```

### 1.5. Python 引号

python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须是相同类型的。  

其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。

```py
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""
```

### 1.6. Python注释

单行注释采用 # 开头。  

```py
# 第一个注释
print ("Hello, Python!")  # 第二个注释
```

python 中多行注释使用三个单引号(''')或三个双引号(""")。  

```py
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
```

### 1.7. Python空行

函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。  

类和函数入口之间也用一行空行分隔，以突出函数入口的开始。  

空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。  

记住：空行也是程序代码的一部分。  

### 1.8. 等待用户输入

\n 实现换行。一旦用户按下 enter(回车) 键退出，其它键显示。

```py
raw_input("按下 enter 键退出，其他任意键显示...\n")
```

### 1.9. 同一行显示多条语句

Python可以在同一行中使用多条语句，语句之间使用分号(;)分割

```py
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
```

### 1.10. print 输出

print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号.  

```py
x="a"
y="b"
# 换行输出
print x
print y

print '---------'
# 不换行输出
print x,
print y,

# 不换行输出
print x,y
```

### 1.11. 多个语句构成代码组

缩进相同的一组语句构成一个代码块，我们称之代码组。  

像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。  

```py
if expression : 
   suite 
elif expression :  
   suite  
else :  
   suite
```

### 1.12. 命令行参数

很多程序可以执行一些操作来查看一些基本信息，Python 可以使用 -h 参数查看各参数帮助信息：

```text
$ python -h 
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ... 
Options and arguments (and corresponding environment variables): 
-c cmd : program passed in as string (terminates option list) 
-d     : debug output from parser (also PYTHONDEBUG=x) 
-E     : ignore environment variables (such as PYTHONPATH) 
-h     : print this help message and exit 
```

## 2. Python 变量类型

### 2.1. 变量赋值(demo/demo1.py)

```py
counter = 100; # 赋值整型变量
miles = 1000.0; # 浮点型
name = "John"; # 字符串

print(counter)
print(miles)
print(name)
```

### 2.2. 多个变量赋值(demo/demo1.py)

```py
# 多个变量赋值
a = b = c = 1
print(a,b,c) # 1,1,1

a, b, c = 1, 2, "john"
print(a,b,c) # 1 2 john
```

### 2.3. 标准数据类型

有五个标准的数据类型：

- Numbers（数字）
- String（字符串）
- List（列表）
- Tuple（元组）
- Dictionary（字典）

#### 2.3.1. Python 数字(demos/type/number.py)

Python支持四种不同的数字类型：

- 整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。
- 长整型(long integers) - 无限大小的整数，整数最后是一个大写或小写的L。
- 浮点型(floating point real values) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 10^2 = 250）
- 复数(complex numbers) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

##### Number 类型转换

int(x [,base ])         将x转换为一个整数  
long(x [,base ])        将x转换为一个长整数  
float(x )               将x转换到一个浮点数  
complex(real [,imag ])  创建一个复数  
str(x )                 将对象 x 转换为字符串  
repr(x )                将对象 x 转换为表达式字符串  
eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象  
tuple(s )               将序列 s 转换为一个元组  
list(s )                将序列 s 转换为一个列表  
chr(x )                 将一个整数转换为一个字符  
unichr(x )              将一个整数转换为Unicode字符  
ord(x )                 将一个字符转换为它的整数值  
hex(x )                 将一个整数转换为一个十六进制字符串  
oct(x )                 将一个整数转换为一个八进制字符串  

##### math 模块、cmath 模块

Python math 模块提供了许多对浮点数的数学运算函数。  

Python cmath 模块包含了一些用于复数运算的函数。  

要使用 math 或 cmath 函数必须先导入：  

```py
import cmath

print(cmath.sqrt(-1))
print(cmath.sqrt(9))
print(cmath.sin(1))
print(cmath.log10(100))

# 1j
# (3+0j)
# (0.8414709848078965+0j)
# (2+0j)
```

##### 数学函数

![数学函数](images/py11.png)

##### Python随机数函数

随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。  

Python包含以下常用随机数函数：  

![随机数函数](images/py12.png)

##### Python三角函数

![三角函数](images/py13.png)

##### Python数学常量

pi —— 数学常量 pi（圆周率，一般以π来表示）。  
e —— 数学常量 e，e即自然常数（自然常数）。  

#### 2.3.2. Python字符串(demo/type/string.py)

字符串或串(String)是由数字、字母、下划线组成的一串字符。  

python的字串列表有2种取值顺序:  

- 从左到右索引默认0开始的，最大范围是字符串长度少1
- 从右到左索引默认-1开始的，最大范围是字符串开头  

如果你要实现从字符串中获取一段子字符串的话，可以使用 [头下标:尾下标] 来截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。  

[头下标:尾下标] 获取的子字符串包含头下标的字符，但不包含尾下标的字符。  

```py
s = 'abcdef'
s[1:5] #'bcde'
```

加号（+）是字符串连接运算符，星号（*）是重复操作。

```py
str = 'Hello World!'
 
print(str * 2)       # 输出字符串两次 Hello World!Hello World!
print(str + "TEST")  # 输出连接的字符串 Hello World!TEST
```

Python 列表截取可以接收第三个参数，参数作用是截取的步长.  
以下在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：  

```py
str = 'Hello World!'
print(str[2:5:2])      # lo
```

##### 转义字符

在需要在字符中使用特殊字符时，python 用反斜杠 \ 转义字符。如下表：  

![转义字符](images/py14.png)

##### 字符串运算符

下表实例变量 a 值为字符串 "Hello"，b 变量值为 "Python"：  

![字符串运算符](images/py15.png)

##### 字符串格式化

将一个值插入到一个有字符串格式符 %s 的字符串中。  

```py
print("My name is %s and weight is %d kg!" % ('Zara', 21))
# My name is Zara and weight is 21 kg!
```

python 字符串格式化符号:  

![字符串格式化符号](images/py16.png)

格式化操作符辅助指令:

![格式化操作符辅助指令](images/py17.png)

##### 三引号

三引号可以将复杂的字符串进行赋值。  

三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。  

三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）。  

```py
hi = '''hi 
there'''
print(hi)

# hi 
# there
```

##### Unicode 字符串

引号前小写的"u"表示这里创建的是一个 Unicode 字符串。如果你想加入一个特殊字符，可以使用 Python 的 Unicode-Escape 编码。如下例所示：

```py
print(u'Hello World !')       # Hello World !
print(u'Hello\u0020World !')  # Hello World !s
```

##### 字符串内建函数

![字符串内建函数](images/py18.png)
![字符串内建函数](images/py19.png)
![字符串内建函数](images/py20.png)

#### 2.3.3. Python列表(demo/type/list.py)

列表用 [ ] 标识, 列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。

列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。  

加号 + 是列表连接运算符，星号 * 是重复操作

```py
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print(list)                # 输出完整列表 ['runoob', 786, 2.23, 'john', 70.2]
print(list[0])             # 输出列表的第一个元素 runoob
print(list[1:3])           # 输出第二个至第三个元素  [786, 2.23]
print(list[2:])            # 输出从第三个开始至列表末尾的所有元素 [2.23, 'john', 70.2]
print(tinylist * 2)        # 输出列表两次 [123, 'john', 123, 'john']
print(list + tinylist)     # 打印组合的列表 ['runoob', 786, 2.23, 'john', 70.2, 123, 'john']
```

##### 更新列表

使用append()方法来添加列表项  

```py
list = []  # 空列表
list.append('Google')  # 使用 append() 添加元素
list.append('Runoob')
print(list) # ['Google', 'Runoob']
```

##### 删除列表元素

使用 del 语句来删除列表的元素

```py
list1 = ['physics', 'chemistry', 1997, 2000]

del list1[2]
print(list1) # ['physics', 'chemistry', 2000]
```

##### 列表脚本操作符

+号用于组合列表，*号用于重复列表。  

![列表脚本操作符](images/py21.png)

##### 列表函数&方法

![列表函数&方法](images/py22.png)
![列表函数&方法](images/py23.png)

python 3.4.3 的版本中已经没有cmp函数，被operator模块代替，在交互模式下使用时，需要导入模块。  

```py
import operator              #首先要导入运算符模块
print(operator.gt(1,2))  # False    #意思是greater than（大于）
print(operator.ge(1,2))  # False    #意思是greater and equal（大于等于）
print(operator.eq(1,2))  # False    #意思是equal（等于）
print(operator.le(1,2))  # True     #意思是less and equal（小于等于）
print(operator.lt(1,2))  # True     #意思是less than（小于）
```

#### 2.3.4. Python 元组(demos/type/tup.py)

元组是另一个数据类型，类似于 List（列表）。  
元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。

```py
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
 
print(tuple)                # 输出完整元组 ('runoob', 786, 2.23, 'john', 70.2)
print(tuple[0])             # 输出元组的第一个元素 runoob
print(tuple[1:3])           # 输出第二个至第四个（不包含）的元素 (786, 2.23)
print(tuple[2:])            # 输出从第三个开始至列表末尾的所有元素 (2.23, 'john', 70.2)
print(tinytuple * 2)        # 输出元组两次 (123, 'john', 123, 'john')
print(tuple + tinytuple)    # 打印组合的元组 ('runoob', 786, 2.23, 'john', 70.2, 123, 'john')
```

创建空元组  

```py
tup1 = ()
```

元组中只包含一个元素时，需要在元素后面添加逗号

```py
tup1 = (50,)
```

##### 访问元组

元组可以使用下标索引来访问元组中的值

```py
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print(tup1[0])    # physics
print(tup2[1:5])  # (2, 3, 4, 5)
```

##### 修改元组

元组中的元素值是不允许修改的，但我们可以对元组进行连接组合

```py
tup3 = tup1 + tup2
print(tup3) # ('physics', 'chemistry', 1997, 2000, 1, 2, 3, 4, 5, 6, 7)
```

##### 删除元组

元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组

元组被删除后，输出变量会有异常信息，输出如下所示：NameError: name 'tup' is not defined

##### 元组运算符

![元组运算符](images/py24.png)

#### 元组内置函数

len(tuple) 计算元组元素个数。  
max(tuple) 返回元组中元素最大值。  
min(tuple) 返回元组中元素最小值。  
tuple(seq) 将列表转换为元组。  

#### 2.3.5. Python 字典(demo/demo5.py)

字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。  

两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。  

字典用"{ }"标识。字典由索引(key)和它对应的值value组成。  

```py
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # 输出键为'one' 的值  #This is one
print(dict[2])  # 输出键为 2 的值  #This is two
print(tinydict)  # 输出完整的字典  #{'name': 'runoob', 'code': 6734, 'dept': 'sales'}
print(tinydict.keys())  # 输出所有键  #dict_keys(['name', 'code', 'dept'])
print(tinydict.values())  # 输出所有值  #dict_values(['runoob', 6734, 'sales'])
```

##### 访问字典里的值

把相应的键放入熟悉的方括弧

```py
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
 
print ("dict['Name']: ", dict['Name'])  # dict['Name']:  Zara
```

##### 修改字典

向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对

```py
dict['Age'] = 8 # 更新
dict['School'] = "RUNOOB" # 添加
 
print( "dict['Age']: ", dict['Age'])        # dict['Age']:  8
print( "dict['School']: ", dict['School'])  # dict['School']:  RUNOOB
```

##### 删除字典元素

能删单一的元素也能清空字典

```py
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
 
del dict['Name']    # 删除键是'Name'的条目  {'Age': 7, 'Class': 'First'}
dict.clear()        # 清空字典所有条目       {}
del dict            # 删除字典              <class 'dict'>
```

##### 字典键的特性

1. 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住

```py
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'} 
print(dict['Name']) # Manni
```

2. 键必须不可变，所以可以用数字，字符串或元组充当

```py
dict = {['Name']: 'Zara', 'Age': 7} 
 
print (dict['Name']) # TypeError unhashable type: 'list'
```

##### 字典内置函数&方法

内置函数：  

len(dict) 计算字典元素个数，即键的总数。  
str(dict) 输出字典可打印的字符串表示。  
type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型。

内置方法:

![内置方法](images/py25.png)

Python3没有dict.has_key方法, 用in  

#### 2.3.6. Python数据类型转换

![数据类型转换](images/py2.png)

## 3. Python 运算符

### 3.1. Python算术运算符(demo/demo6.py)

![算术运算符](images/py3.png)

```py
a = 2
b = 3
c = a**b 
print("c 的值为：", c)
 
a = 10
b = 5
c = a//b 
print("c 的值为：", c)
```

### 3.2. Python比较运算符(demo/demo7.py)

![比较运算符](images/py4.png)

### 3.3. Python赋值运算符(demo/demo8.py)

![赋值运算符](images/py5.png)

### 3.4. Python位运算符(demo/demo9.py)

按位运算符是把数字看作二进制来进行计算的.  

![赋值运算符](images/py6.png)

### 3.5. Python逻辑运算符(demo/demo10.py)

![逻辑运算符](images/py7.png)

```py
a = 10
b = 20

print("a and b", a and b) # 20

print("a or b", a or b) # 10

print("not b", not a) # False
```

### 3.6. Python成员运算符(demo/demo11.py)

![成员运算符](images/py8.png)

```py
a = 10
b = 20
list = [1, 2, 3, 4, 5]

print("a in list", a in list)               # False
print("b not in list", b not in list)       # True
```

### 3.7. Python身份运算符(demo/demo12.py)

身份运算符用于比较两个对象的存储单元  

![身份运算符](images/py9.png)

```py
a = 20
b = 20

print("a is b", a is b)             #  True
print("a is not b", a is not b)     #  False
```

### 3.8. Python运算符优先级

![运算符优先级](images/py10.png)

## 4. Python 条件语句(demo/demo13.py)

if 语句用于控制程序的执行，基本形式为：  

```text
if 判断条件：
    执行语句……
else：
    执行语句……
```

```py
flag = False
name = 'luren'
if name == 'python':  # 判断变量是否为 python
    flag = True  # 条件成立时设置标志为真
    print('welcome')  # 并输出欢迎信息
else:
    print(name)  # 条件不成立时输出变量名称
```

当判断条件为多个值时，可以使用以下形式：  

```text
if 判断条件1:
    执行语句1……
elif 判断条件2:
    执行语句2……
elif 判断条件3:
    执行语句3……
else:
    执行语句4……
```

```py
num = 5
if num == 3:  # 判断num的值
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:  # 值小于零时输出
    print('error')
else:
    print('roadman')  # 条件均不成立时输出
```

如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。  

```py
num = 9
if num >= 0 and num <= 10:  # 判断值是否在0~10之间
    print('hello')
# 输出结果: hello
num = 10
if num < 0 or num > 10:  # 判断值是否在小于0或大于10
    print('hello')
else:
    print('undefine')
# 输出结果: undefine

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print('hello')
else:
    print('undefine')
# 输出结果: undefine
```

可以在同一行的位置上使用if条件判断语句

```py
var = 100
if (var == 100): print("变量 var 的值为100")
```

## 5. Python 循环语句(demos/demo14.py)

Python 提供了 for 循环和 while 循环（在 Python 中没有 do..while 循环）。  

while 循环——在给定的判断条件为 true 时执行循环体，否则退出循环体。  
for 循环——重复执行语句。  
嵌套循环——你可以在while循环体中嵌套for循环。  

循环控制语句可以更改语句执行的顺序。Python支持以下循环控制语句。  

break 语句——在语句块执行过程中终止循环，并且跳出整个循环。  
continue 语句——在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。  
pass 语句——pass是空语句，是为了保持程序结构的完整性。  

### 5.1. While 循环语句

其基本形式为：

```text
while 判断条件(condition)：
    执行语句(statements)……
```

```py
count = 0
while (count < 9):
    print('The count is:', count)
    count = count + 1

print("Good bye!")
```

while 语句时还有另外两个重要的命令 continue，break 来跳过循环，continue 用于跳过该次循环，break 则是用于退出循环，此外"判断条件"还可以是个常值，表示循环必定成立，具体用法如下：  

```py
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print(i)  # 输出双数2、4、6、8、10

i = 1
while 1:  # 循环条件为1必定成立
    print(i)  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break
```

#### 5.1.1. 无限循环

如果条件判断语句永远为 true，循环将会无限的执行下去

```py
var = 1
while var == 1 :  # 该条件永远为true，循环将无限执行下去
   num = raw_input("Enter a number  :")
   print ("You entered: ", num)
 
print ("Good bye!")
```

#### 5.1.2. 循环使用 else 语句

在 python 中，while … else 在循环条件为 false 时执行 else 语句块：

```py
count = 0
while count < 5:
    print(count, " is  less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")
```

#### 5.1.3. 简单语句组

如果你的 while 循环体中只有一条语句，你可以将该语句与while写在同一行中

```py
flag = 1
while (flag): print ('Given flag is really true!')
print ("Good bye!")
```

### 5.2. for 循环语句

for循环的语法格式如下：

```text
for iterating_var in sequence:
   statements(s)
```

```py
for letter in 'Python': 
    print('当前字母 :', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits: 
    print('当前水果 :', fruit)
```

#### 5.2.1. 通过序列索引迭代

```py
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('当前水果 :', fruits[index])
```

#### 5.2.2. 循环使用 else 语句

for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。  

```py
for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print(num, '是一个质数')
```

### 5.3. 循环嵌套

Python for 循环嵌套语法：

```text
for iterating_var in sequence:
   for iterating_var in sequence:
      statements(s)
   statements(s)
```

Python while 循环嵌套语法：

```text
while expression:
   while expression:
      statement(s)
   statement(s)
```

```py
# 嵌套循环输出2~100之间的素数：
i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print(i, " 是素数")
    i = i + 1
```

### 5.4. break 语句

break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。

```py
for letter in 'Python':
    if letter == 'h':
        break
    print('当前字母 :', letter)
# 当前字母 : P
# 当前字母 : y
# 当前字母 : t
```

### 5.5. continue 语句

continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。  

continue语句用在while和for循环中。  

```py
for letter in 'Python':
    if letter == 'h':
        continue
    print('当前字母 :', letter)
# 当前字母 : P
# 当前字母 : y
# 当前字母 : t
# 当前字母 : o
# 当前字母 : n
```

## 6. pass语句(demos/demo15.py)

Python pass 是空语句，是为了保持程序结构的完整性。  

pass 不做任何事情，一般用做占位语句。  

```py
for letter in 'Python':
    if letter == 'h':
        pass
        print('这是 pass 块')
    print('当前字母 :', letter)
# 当前字母 : P
# 当前字母 : y
# 当前字母 : t
# 这是 pass 块
# 当前字母 : h
# 当前字母 : o
# 当前字母 : n
```

## 7. 日期和时间

