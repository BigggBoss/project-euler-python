# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 22:34:48 2017

@author: Pei
"""
import time

stime = time.time()
now_num = 0
total_loc = 0
target_loc_list = [1, 10, 100, 1000, 10000, 100000, 1000000]
target_index = 0
result = 1

def getDigits(num):
    result = 1
    while int(num/10) > 0:
        result += 1
        num = int(num/10)
    return result

def getNumLoc(num, loc):
    return int(str(num)[-loc])

while target_index <= len(target_loc_list) - 1:
    now_num += 1
#    total_loc += getDigits(now_num)
    total_loc += len(str(now_num))
    if total_loc >= target_loc_list[target_index]:
        print('The ' + str(target_index) + 'th number is ' + str(getNumLoc(now_num, total_loc - target_loc_list[target_index] + 1)) + '.')
        result = result * getNumLoc(now_num, total_loc - target_loc_list[target_index] + 1)
        target_index += 1
print('result is ', result)
print(time.time() - stime)
