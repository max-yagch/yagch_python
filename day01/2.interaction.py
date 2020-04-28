# -*- coding: utf-8 -*-

name = input("name:")
job = input("job:")
salary = input("salary:")

# 1、变量引用     shell $变量名
# %s string
# %d 数字
# %f 浮点


# 格式化输出不要使用拼接字符串  会开辟多块内存 效率低下


# 强制转数据类型
age = int(input("age:"))

# 格式化输出
info = '''
-----info of %s -------
name:%s
age:%d
job:%s
salary:%s
'''%(name,name,age,job,salary)
# print(info)

# 默认所有的输入都是字符串
# print(type(age))


# 推荐使用这种格式化
info2 = '''
-----info of {_name} -------
name:{_name}
age:{_age}
job:{_job}
salary:{_salary}
'''.format(_name=name,_age=age,_job=job,_salary=salary)
# python3里的input和python2里的raw_input效果一样
# python2 里input不要用
# print(info2)

# 格式化输出
info3 = '''
-----info of {0} -------
name:{0}
age:{1}
job:{2}
salary:{3}
'''.format(name,age,job,salary)