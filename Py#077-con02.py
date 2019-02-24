# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 10:31:58 2019

@author: LIZY52
"""

list1 = ['背光点亮','背光黯灭']
list2 = ['自动','制冷','抽湿','送风','制热']

'''
for i in list1:
    print('1.',i)   
for j in list2:
    print('2.',j)
'''

for i in list1:
    for j in list2:
        print("1.%s" % i)      
        print("2.当前模式为%s" % j)
        print("")       