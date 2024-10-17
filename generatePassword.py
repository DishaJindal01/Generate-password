
#also using list comprihension
# used when we want to call funtions again and again and put all in a list

import random
import string
val_str= string.ascii_letters + string.punctuation + string.digits
print(type(val_str))   # its of string datatype
val = ""
for i in range(12):
    val += random.choice(val_str)
print("random password generated:",val)

# list comprehension using

# k =[random.choice(val_str) for i in range(12)]
# print(k)

