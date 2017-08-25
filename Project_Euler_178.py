# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 21:03:12 2017

@author: Pei
"""

'''
Step Numbers
Problem 178 

Consider the number 45656. 
It can be seen that each pair of consecutive digits of 45656 has a difference of one.
A number for which every pair of consecutive digits has a difference of one is called a step number.
A pandigital number contains every decimal digit from 0 to 9 at least once.
How many pandigital step numbers less than 1040 are there?
'''

import time
import pdb

stime = time.time()

# 字符变为index
def getLv0Index(str_like):
    result = ''
    temp = list(set(list(str_like)))
    temp.sort()
    for i in temp:
        result = result + i
    return result

# dic 中加入元素
def addNum2Dic(dic, key0, key1, value):
    if key0 in dic.keys():
        if key1 in dic[key0].keys():
            dic[key0][key1] = dic[key0][key1] + value
        else:
            dic[key0][key1] = value
    else:
        dic[key0] = {key1 : value}
    return dic


# step number 增加一位， 获得新的dic
def addDigital(sn_dic):
    result_dic = {}
    for key_lv0, value_lv0 in sn_dic.items():
        for key_lv1, value_lv1 in sn_dic[key_lv0].items():
            if key_lv1 != 0:
                new_key_lv0 = getLv0Index(key_lv0 + str(key_lv1 - 1))
                new_key_lv1 = key_lv1 - 1
                result_dic = addNum2Dic(result_dic, new_key_lv0, new_key_lv1, value_lv1)
            if key_lv1 != 9:
                new_key_lv0 = getLv0Index(key_lv0 + str(key_lv1 + 1))
                new_key_lv1 = key_lv1 + 1
                result_dic = addNum2Dic(result_dic, new_key_lv0, new_key_lv1, value_lv1)
    return result_dic

# 计算目前的 Pandigital Number数
def getPandigitalNum(num, steps):
    result = [0]*10
    result[num] = 1
    temp = result.copy()
    for i in range(steps):
        temp_new = [0]*10
        for j in range(10):
            if j != 0:
                temp_new[j] += temp[j - 1]
            if j != 9:
                temp_new[j] += temp[j + 1]
        temp = temp_new.copy()
        for j in range(10):
            result[j] += temp[j]
    return sum(result)

def getResult(digital):
    # 初始 step number 字典
    step_number_dic = {}
    for i in range(1, 10):
        step_number_dic[str(i)] = {i: 1}
    
    result = 0
    for i in range(2, digital+1):
        # step number 增加一位， 获得新的dic
        step_number_dic = addDigital(step_number_dic)
        if '0123456789' in step_number_dic.keys():
            pandigital_num = step_number_dic.pop('0123456789')
            for key, value in pandigital_num.items():
                result += getPandigitalNum(key, digital - i) * value
    return result
        
print(getResult(50))
print(time.time() - stime)


    