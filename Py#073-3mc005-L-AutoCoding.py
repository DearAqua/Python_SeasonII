# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 15:22:02 2018

@author: LIZY52
"""

for i in range(15, 125, 5):
    if i<100:
      print("'Value = %d " % i)
      print('LeftDoubleClick 1')
      print('Delay 500')
      print('KeyPress "Num %d", 1' % (i//10))
      print('KeyPress "Num %d", 1' % (i%10))
      print('Delay 500')
      print('')
      print("\'Send")
      print('KeyPress "Enter", 1')
      print('Delay 500')
      print('KeyPress "Enter", 1')
      print('Delay 5000')
      print('')
    else:
      print("'Value = %d " % i)
      print('LeftDoubleClick 1')
      print('Delay 500')
      print('KeyPress "Num %d", 1' % (i//100))
      print('KeyPress "Num %d", 1' % ((i//10)%10))
      print('KeyPress "Num %d", 1' % (i%10))
      print('Delay 500')
      print('')
      print("\'Send")
      print('KeyPress "Enter", 1')
      print('Delay 500')
      print('KeyPress "Enter", 1')
      print('Delay 5000')
      print('')
      