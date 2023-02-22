import random

title = input("App name : ")

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbol = "{}[];*#@_-"

passkey = lower_case+upper_case+num+symbol

length = 9
password = "".join(random.sample(passkey,length))
print("password is : ",password)

file = open(f"{title}.txt", 'w')
file.write(password)
file.close()