#!/usr/bin/env python
# coding=utf-8
import getpass

# username = raw_input("Please enter the username:")
# papssword = getpass.getpass("Please enter the password:")

# print username
# print password
user = "yinan"
pwd = "13197"

run_forver = True

# while run_forver:
count = 0
for count in range(3):
    username = raw_input("Please enter the username:")
    password = getpass.getpass("Please enter the password:")
    if username == user and password == pwd:
         print("ok,You are right!")
         break
    else:
         print("try again!")

