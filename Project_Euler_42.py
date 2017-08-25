# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 21:04:19 2017

@author: Pei
"""

'''
Coded triangle numbers
Problem 42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

import math
import time

stime = time.time()

file = open('C:/Users/Pei/Desktop/p042_words.txt')
words = file.readline()
words = words.replace('\"', '').split(",")
file.close()
triangle_words_num = 0

def isTriangleNum(num):
    num = 2 * num
    num_sqrt = int(math.sqrt(num))
    if num_sqrt * (num_sqrt + 1) == num:
        return True
    else:
        return False
    
for word in words:
    word_num = 0
    for i in range(len(word)):
        word_num += ord(word[i]) - 64
    if isTriangleNum(word_num):
        triangle_words_num += 1

print(triangle_words_num)
print(time.time() - stime)


