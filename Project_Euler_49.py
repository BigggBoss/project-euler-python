# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 19:52:36 2017

@author: Pei
"""

'''
Prime permutations
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

import time

stime = time.time()
prime_list = [2]

for i in range(3, 10000):
    is_prime = True
    for prime in prime_list:
        if i % prime == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(i)

result = []
for prime in prime_list:
    if prime > 999:
        result.append(prime)

prime_list = result.copy()
def getResult(prime_list):
    result = []
    for i in range(len(prime_list) - 2):
        for j in range(i + 1, len(prime_list) - 1):
            p3 = prime_list[j] * 2 - prime_list[i]
            if p3 in prime_list:
                p1 = list(str(prime_list[j]))
                p1.sort()
                p2 = list(str(prime_list[i]))
                p2.sort()
                p3 = list(str(p3))
                p3.sort()
                if p1 == p2 and p2 == p3:
                    result.append([prime_list[i], prime_list[j], prime_list[j] * 2 - prime_list[i]])
                    if len(result) == 2:
                        return result
    return result

result = getResult(prime_list)
print(result)
print(time.time() - stime)






stime = time.time()

def minnum(num):
    temp = list(str(num))
    temp.sort()
    result = ''
    for i in range(len(temp)):
        result = result + temp[i]
    return int(result)

def isResult(list_like):
    for i in range(len(list_like) - 2):
        for j in range(i + 1, len(list_like) - 1):
            for k in range(j + 1, len(list_like)):
                if list_like[i][1] + list_like[k][1] == 2*list_like[j][1]:
                    return int(str(list_like[i][1]) + str(list_like[j][1]) + str(list_like[k][1]))
    return False
    
def getResult():
    result = []
    prime_list = [[2, 2]]
    for i in range(3, 10000):
        is_prime = True
        for prime in prime_list:
            if i % prime[1] == 0:
                is_prime = False
                break
        if is_prime:
            if prime_list[-1][1] // 1000 == 0 and i // 1000 > 0:
                first_index = len(prime_list)
            prime_list.append([minnum(i), i])
    
    prime_list = prime_list[first_index:]
    prime_list.sort()
    
    j = 0
    while i < len(prime_list) - 1:
        i = j
        j = i + 1
        while j < len(prime_list):
            if prime_list[i][0] == prime_list[j][0]:
                j += 1
            elif j - i >= 3:
                result_one = isResult(prime_list[i:j])
                if result_one:
                    result.append(result_one)
                    if len(result) == 2:
                        return result
                break
            else: break

result = getResult()
print(result)
print(time.time() - stime)
