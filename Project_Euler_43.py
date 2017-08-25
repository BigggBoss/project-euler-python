# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 09:14:13 2017

@author: Pei
"""


'''
Sub-string divisibility
Problem 43 
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''

import time

stime = time.time()
digit_set = set(list('0123456789'))
result = []
for i in range(1, int(999/17) + 1):
    if i <= 5:
        result.append('0' + str(i * 17))
        next
    if len(set(list(str(i * 17)))) == 3:
        result.append(str(i * 17))

div_list = [13, 11, 7, 5, 3, 2]
for i in range(6):
    temp = []
    for num_last_i in result:
        for num in digit_set - set(num_last_i):
            if int(num + num_last_i[:2]) % div_list[i] == 0:
                temp.append(num + num_last_i)
    result = temp.copy()

for i, num in enumerate(result):
    for j in digit_set - set(list(num)):
        result[i] = int(j + num)

print(sum(result))
print(time.time() - stime)
