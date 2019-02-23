# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 10:23:35 2019

@author: LIZY52
"""

'''
import itertools



list1 = 'abc'

list2 = []



for i in range(1,len(list1)+1):

    iter = itertools.combinations(list1,i)

    list2.append(list(iter))



print(list2)
'''
def lists_combination(lists, code=''):
    '''输入多个列表组成的列表, 输出其中每个列表所有元素可能的所有排列组合
    code用于分隔每个元素'''
    try:
        import reduce
    except:
        from functools import reduce
        
    def myfunc(list1, list2):
        return [str(i)+code+str(j) for i in list1 for j in list2]
    return reduce(myfunc, lists)

'''

list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]

res = lists_combination([list1, list2, list3])
print(res)

'''

list1 = ['背光点亮','背光黯灭']
list2 = [' ']
list3 = ['自动','制冷','抽湿','送风','制热']

res = lists_combination([list1, list2, list3])
print(res)