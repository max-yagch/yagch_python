# -*- coding: utf-8 -*-



yagch_age = 25
"""
count = 0
while count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == yagch_age:
        print("yes")
        break
    elif guess_age > yagch_age:
        print("large")
    else:
        print("smaller")
    count = count + 1
else:
    print("too many times")
"""

# 函数可创建一个整数列表，一般用在 for 循环中
# 参数说明
# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)


for i in range(3):
    guess_age = int(input("guess age:"))
    if guess_age == yagch_age:
        print("yes")
        break
    elif guess_age > yagch_age:
        print("large")
    else:
        print("smaller")
else:
    print("too many times")