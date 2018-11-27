# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:06:13 2018

@author: LIZY52
"""

for i in range(20, 60):
    if i<10:
        print("\'Value =",i," --> Temperature =",i)
        print('')
        print('LeftDoubleClick 1')
        print('Delay 500')       
        print('KeyPress "Num %d", 1' % i)
        print('Delay 500')
        print('KeyPress "Enter", 1')
        print('Delay 1000')
        print('KeyPress "Enter", 1')
        print('Delay 10000')
        print('')
    elif i<100:
        print("\'Value =",i," --> Temperature =",i)
        print('')
        print('LeftDoubleClick 1')
        print('Delay 500')       
        print('KeyPress "Num %d", 1' % (i//10))
        print('KeyPress "Num %d", 1' % (i%10))
        print('Delay 500')
        print('KeyPress "Enter", 1')
        print('Delay 1000')
        print('KeyPress "Enter", 1')
        print('Delay 10000')
        print('')