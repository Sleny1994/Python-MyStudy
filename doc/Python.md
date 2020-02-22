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
- 内置BIF，open()函数就是用于与文件交互，与for循环结合使用，可以对文件内容进行读取

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



## 异常

### 用法

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

