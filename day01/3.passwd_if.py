# -*- coding: utf-8 -*-

import getpass


_username = "yang"
_password = "chong"
# 明文
username = input("username:")
password = input("password:")
if username==_username and password == _password:
    print("welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password")


# 密文密码  getpass 在pycharm中不能用,别的地方能用
# username = input("username:")
# password = getpass.getpass("password:")
# print(username,password)
