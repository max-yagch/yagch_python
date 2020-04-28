# -*- coding: utf-8 -*-

yagch_age = 25

guess_age = int(input("guess age:"))

if guess_age == yagch_age :
    print("yes")
elif guess_age > yagch_age :
    print("large")
else:
    print("smaller")