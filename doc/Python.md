# Python

## 字符串

### 定义

- 在一个字符串中嵌入一个双引号，可以使用转义符\，或者使用单引号引起这个字符串
```Python
str1 = 'I am "Sleny".'
str2 = 'I am \"Sleny\".'
```
### 方法

- split()函数可以分割字符串，默认不对分割部分数做限制，但存在可选参数maxsplit，默认为-1
- find()函数可以找出字符串中的子串，如果无法找到返回值为-1，如果找到则返回子串在原字符串中的索引值
- strip()函数可以将字符串两边的空白符去除
- str()函数可以将数据对象字符串化
- in操作用于检查成员关系，可以确定该成员是否在数据对象中
- pop(index = -1)函数可以删除列表中的某个数据，默认为最后一项

---

## 列表

### 定义

- list = ["Apple", "Perl", "Orange"]
- 列表类似于数组，列表可以包含混合类型的数据，同样包括列表，即列表内可以嵌套列表
```Python
lists = [A,B,C,[D,E,F,[i,j]]]
```
- 列表不支持越界检查，但如果访问一个不存在的数据项，Python会给出一个IndexError的错误响应

### 增加

- list.append("Sleny") --该方法会将数据增加至列表的末尾
- list.insert(1, "Zl") --该方法会在Apple后增加该值
- list.extend([1,2,3]) --该方法会将新的列表扩展至原有列表中

### 排序

- list.sort() --该方法提供原地排序，Python内置BIF中使用sorted()方法来提供复制排序，两种排序方式默认均是升序，若需要降序则需要传入参数reverse=True

### 推导

- 列表推导是为了减少将一个列表转换为另一个列表时所需的代码，可以将原有的四行代码缩减为一行，且不需要再单独使用append()方法
```Python
new_list = [sanitize(each_t) for each_t in old_list]
# new_list:    新生成的列表
# old_list:    原有的列表
# each_t:      需要迭代的目标标识符
# sanitize():  转换函数
```

---

## 集合

### 定义
- 集合中的数据是无序的且不允许重复的

---

## 字典

### 定义
- Python内置的数据结构，使用key-value格式关联数据
- 以{}的形式出现，或者可以使用dict()BIF创建
- 支持动态扩展
```Python
dict = {"A":1, "B":2, "C":3}
print(dict["A"])

---output---
1
```

---

## 循环

### for循环

- for循环是可伸缩的，适用于任意大小的列表
- 从列表的起始位置开始，一直处理到列表的末尾
```Python
lists = ['A', 'B', 'C', ['D', 'E', 'F', ['i', 'j']]]
for pic in lists:
	if isinstance(pic, list):
		for pic_2 in pic:
			print(pic_2)
	else:
		print(pic)

# 这样对于深层嵌套列表[i, j]并未能够将其逐个输出，是否是再写入一个if..else..呢？如果只有一层两层还好，要是上百层呢？重复性的代码输入，会让你的代码看起来非常冗长，所以不如试试函数吧。
```

### while循环
- 与for循环类似，但需要考虑到状态信息，即需要使用计数标识符

---

## 函数

### 内置函数

- Python Shell中输入dir(__builtins__)即可输出内置函数的列表，help()函数则可以输出单个BIF的功能描述
- isinstance() 用于检查某个特定标识符是否包含某个特定类型的数据
- range()，可以提供需要控制来迭代的次数，生成一个从0开始到某个数的数字列表  
```Python
# 添加一个参数，使该函数可以在发现一个嵌套列表时缩进一个TAB，两个则缩进两个TAB
def print_list(lists, level):
	for each_list in lists:
		if isinstance(each_list, list):
			print_list(each_list, level + 1) # 递归调用该函数
		else:
            for i in range(level):
                print("\t", end = '')
			print(each_list)

print_list(lists, 0)
```

- os()，主要用于提供系统层级的操作

```Python
import os
os.getcwd() # 可以查看当前工作目录
os.chdir('C:\\') # 切换工作目录
os.path.exists() # 用于确认该路径/文件是否存在
```

- print()，主要用于打印输出，参数添加end = ''则可以取消换行
- locals()，会返回当前作用域中定义的所有名的一个集合
- String模块中包含一个名为Template的类，可以用于简单的字符串替换

### 自定义函数

- 标准形式：
```Python
def function_name(object):
    func_body

# 接for循环问题
def print_list(lists):
	for each_list in lists:
		if isinstance(each_list, list):
			print_list(each_list) # 递归调用该函数
		else:
			print(each_list)

print_list(lists)
```

### 可选参数
- 对参数设置一个缺省值，即object = xx

---

## 注释

### 单行注释

- \# 用于单行注释

### 多行注释

- """""" 三重引号用于多行注释

---

## 模块

### 定义

- 模块就是一个包含Python代码的文本文件，以.py结尾
- Python包索引（Python Package Index， PyPI），第三方模块聚集地
- import sys; sys.path 可以输出一个列表，内包含了Python的安装路径以及模块存储路径

### 发布

1. 函数模块创建完成后，需要创建一个新的文件夹，将函数模块文件放入其中
2. 在该文件夹中创建一个setup.py文件，并添加相关内容如下
```Python
from distutils.core import setup

setup(
    name         = 'nester',
    version      = '1.0.0',
    py_modules   = ['nester'],
    author       = 'sleny',
    author_email = 'sleny@qq.com',
    url          = 'http://www.zlcode.pub',
    description  = 'A simple printer of nested lists',)
```
3. 使用命令构建一个发布文件
```Python
python setup.py sdist
```
4. 使用命令将发布文件安装至本地副本
```Python
python setup.py install
```
5. 访问PyPI网站（http://pypi.python.org/），注册请求一个PyPI ID
6. 使用命令行登录PyPI，根据提示输入用户名与密码
```Python
python setup.py register
```
7. 使用命令上传发布文件
```Python
python setup.py sdist upload
```

### 导入

- 使用'import'关键字导入模块

### 命名空间

- Python中所有的代码都与一个命名空间关联，主程序\_\_main\_\_，内置函数\_\_builtins\_\_
- 当将代码放入单独的模块中时，Python会自动创建一个与模块同名的命名空间
- space_name.function_name(object)，则可以正常调用模块内的函数，这种叫做命名空间限定

***注***
- from lib_name import function_name，则可以将指定的函数增加到当前的命名空间，这样就不需要使用命名空间限定，但如果你的当前命名空间内已经有一个同名函数，则会导致导入的函数覆盖你此前已有的同名函数

---

## 文件

### 定义
- Python中的基本输入机制是基于行的
- 内置BIF，open()函数就是用于与文件交互，与for循环结合使用，可以对文件内容进行读取，一般默认使用r参数表示读

```Python
data = open('sketch.txt') # 打开文件sketch.txt
print(data.readline()) # 使用readline()函数逐行读取文件内的内容，并print出来
data.seek(0) # 使用seek()函数返回到文件起始位置，也可以使用tell()
for lines in data:
    print(lines) # for循环，逐行打印
    (role, spoken) = lines.split(":") # split()函数可以按照要求分割字符串，并将分割的左右两边分别赋值
	print(role, end='')
	print(" said:", end='')
	print(spoken, end='')
data.close() # 操作文件结束后，关闭文件
```

### 存储
- open("filename", "w")，使用w用来表示写模式，如果filename文件已经存在，则会覆盖该文件清楚原有所有内容，若要追加某文件则需要使用a模式，要写和读则需要使用w+模式。
```Python
out = open("Filename.txt", "w")
print("Something is writed in Filename.", file = out) # 前者需要写入的内容，后者指定写入的对象
out.close()

---

import os

man = []
other = []

try:
    data = open('sketch.txt')    
    for lines in data:
        try:
            (role, spoken) = lines.split(":", maxsplit = 1)
            spoken = spoken.strip()
            if role == 'Man':
                man.append(spoken)
            elif role == 'Other Man':
                other.append(spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print("This file is missing.")

try:
    man_file = open("man_data.txt", "w")
    other_file = open("other_data.txt", "w")
    print(man, file = man_file) # 必须写file = 
    print(other, file = other_file) # 执行时shell里没有输出，但文件内会产生两个文件，其内有对应的内容
    man_file.close()
    other_file.close()
except IOError:
    print("Failed!")
```
- 标准输出（standard output），即sys.stdout，print()的默认参数即为此
- 标准错误输出(STDERR)，即sys.stderr，修改print()函数的file参数将其重定向到stderr则可打印错误输出

### Pickle

- pickle模块，Python专用数据存储方式，该方式必须以二进制的模式打开这些文件即wb和rb

```Python
import pickle

try:
	with open("mydata.pickle", "wb") as mysavedata:
    	pickle.dump([1,2,3,"Hello"], mysavedata) # 使用pickle.dump()保存数据
	with open("mydata.pickle", "rb") as myresdata:
    	new_list = pickle.load(myresdata) # 使用pickle.load()读取数据
    	print(new_list)
except PickleError as pic_err:
    print("Picking error: " + str(pic_err))
```

- 如果pickle保存或读取数据时出现问题，会产生一个PickleError类型的异常

---

## 异常

### 用法

#### 一般异常处理

```Python
try:
    your code
except:
    error code

e.g:
data = open('sketch.txt')    
for lines in data:
	try:
		(role, spoken) = lines.split(":", maxsplit = 1)
		print(role, end='')
		print("said:", end='')
		print(spoken, end='')
	except:
		pass
data.close() 

---output---	
Mansaid: Is this the right room for an argument?
Other Mansaid: I've told you once.
Mansaid: No you haven't.
Other Mansaid: Yes I have.
Mansaid: When?
Other Mansaid: Just now.
Mansaid: No you didn't!
Mansaid: (exasperated) Oh, this is futile!!:OK?
```

#### 指定异常处理

```Python
import os

try:
    data = open('sketch.txt')    
    for lines in data:
        try:
            (role, spoken) = lines.split(":", maxsplit = 1)
            print(role, end='')
            print("said:", end='')
            print(spoken, end='')
        except ValueError: # 指定错误类型
            pass
    data.close()
except IOError: # 指定错误类型
    print("This file is missing.")
```

#### 扩展异常处理

- 当需要不论出现什么错误都必须保证运行某些代码时使用，添加finally

```Python
try:
    man_file = open("man_data.txt", "w")
    other_file = open("other_data.txt", "w")
    print(man, file = man_file) 
    print(other, file = other_file) 
    
except IOError:
    print("Failed!")

finally: # 无论是否出现异常，其下代码均会被执行
    man_file.close()
    other_file.close()
```
- 使用with代替finally减少代码量，产出更优雅的代码，其会自动的处理所有已打开文件的关闭工作

```Python
try:
    with open("man_data.txt", "w") as man_file: # 也可以将两个open合并在一起，使用逗号隔开
        print(man, file = man_file)
    with open("other_data.txt", "w") as other_file:
        print(other, file = other_file)
except IOError as err:
    print("File error: " + str(err))
```



#### 特定异常处理

```python
try:
    
except IOError as err:
    print("File error: " + str(err))
    
---output---
File error: [Error 2] No such file or directory: 'missing.txt'
```

---

## 类

### 定义
- 面向对象中，函数被称为是类的方法，数据则称为类的属性，实例化的数据对象称为实例
- 使用class创建类对象，每个定义的类都有一个特殊的方法，\_\_init\_\_()，主要用于初始化对象，且该方法下不能空着否则会提示缩进错误
```Python
class A:
    def __init__(self):
        # 这里可以初始化各个对象
    def show(self):
        print("Hello World!")

a = A() # 实例化对象
a.show()
```
- 类中定义的所有方法的第一个参数均是self
- @property可以在类中修饰类方法，被修饰过的类方法对于类用户来说则像是一个属性

### 继承
- 通过继承创建的类称为子类，可以继承新创建的类，也可以继承原有的内置类
```Python
class NamedList(list):
    def __init__(self, a_name):
        # list.__init__([]) ,添加该句代码和不添加似乎并无区别
        self.name = a_name

a_list = NamedList("Hello")
# a_list拥有list的所有功能，且还多了name参数
```

---

## Web开发

### 定义

- CGI（Common Gateway Interface），通用网关接口
- MVC（Model View Controller），遵循模式-视图-控制器模式
- webapp下一般包含有文件夹（cgi-bin、data、images、templates），index.html，favicon.ico等不适合放在子文件夹下的文件
- Python可以提供自己的Web服务器，包含在http.server库模块中
- 用Python构建Web服务器必须有下列这五行代码

```Python
from http.server import HTTPServer, CGIHTTPRequestHandler # 导入HTTP服务器和CGI模块

port = 8080 # 指定端口
httpd = HTTPServer(('', port), CGIHTTPRequestHandle) # 创建一个HTTP服务器
print("Starting simple_httpd on port: " + str(httpd.server_port)) # 显示一个友好消息
httpd.server_forever() # 启动服务器
```

- 在不同操作系统上运行WebApp有不同的前期操作需求
  - Windows，无需额外操作
  - 类Unix
    1. 使用chmod+x命令设置CGI的可执行权限
    2. 在程序代码的最上方添加 #! /usr/local/bin/python3

- Python标准库中提供一个CGI的跟踪模块（cgitb），启用这个模块时，会在Web浏览器上显示详细的错误消息

```Python
import cgitb
cgitb.enable()
```

- 可以使用cgi.FieldStorage()访问作为Web请求一部分发送给Web服务器的数据，数据作为一个Python字典

---

## JSON

### 定义

- 基于文本的格式，与语言无关，可使用其它编程语言编写的程序进行交互
- 标准JSON库只能处理Python的内置类型，无法处理自定义的类对象，有时则需要将数据转化为Python的内置数据类型

### 用法

- Python内置有json库，直接导入即可使用其功能，使用方法与pickle类似

```Python
import json

test = ['A', ['B', 'C'], 2, ['D', 'E', 'F']]
to_json = json.dumps(test)
to_test = json.loads(to_json)
```

