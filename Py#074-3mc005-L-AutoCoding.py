# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:57:47 2018

@author: LIZY52
"""

for i in range(-11, 12):
    if i<=-10:
      print("'Value= %d" % i)
      print('LeftDoubleClick 1')
      print('Delay 500')
      print('KeyPress "BackSpace", 1')
      print('KeyPress "BackSpace", 1')
      print('KeyPress "BackSpace", 1')
      print('Delay 500')
      print('KeyPress "Num -", 1')
      print('KeyPress "Num %d", 1' % ((-i)//10))
      print('KeyPress "Num %d", 1' % ((-i)%10))
      print('Delay 500')
      print('')
      print("'Send")
      print('KeyPress "Enter", 1')
      print('Delay 500')
      print('KeyPress "Enter", 1')
      print('Delay 5000')
      print('')
    elif -10<i<0:
      print("'Value= %d" % i)
      print('LeftDoubleClick 1')
      print('Delay 500')
      print('KeyPress "BackSpace", 1')
      print('KeyPress "BackSpace", 1')
      print('KeyPress "BackSpace", 1')
      print('Delay 500')
      print('KeyPress "Num -", 1')
      print('KeyPress "Num %d", 1' % -i)
      print('Delay 500')
      print('')
      print("'Send")
      print('KeyPress "Enter", 1')
      print('Delay 500')
      print('KeyPress "Enter", 1')
      print('Delay 5000')
      print('')
    elif 10>i>=0:
      print("'Value= %d" % i)
      print('LeftDoubleClick 1')
      print('Delay 500')
      print('KeyPress "BackSpace", 1')
      print('KeyPress "BackSpace", 1')
      print('KeyPress "BackSpace", 1')
      print('Delay 500')
      print('KeyPress "Num %d", 1' % i)
      print('Delay 500')
      print('')
      print("'Send")
      print('KeyPress "Enter", 1')
      print('Delay 500')
      print('KeyPress "Enter", 1')
      print('Delay 5000')
      print('')
    elif i>=10:
      print("'Value= %d" % i)
      print('LeftDoubleClick 1')
      print('Delay 500')
      print('KeyPress "BackSpace", 1')
      print('KeyPress "BackSpace", 1')
      print('KeyPress "BackSpace", 1')
      print('Delay 500')
      print('KeyPress "Num %d", 1' % (i//10))
      print('KeyPress "Num %d", 1' % (i%10))
      print('Delay 500')
      print('')
      print("'Send")
      print('KeyPress "Enter", 1')
      print('Delay 500')
      print('KeyPress "Enter", 1')
      print('Delay 5000')
      print('')