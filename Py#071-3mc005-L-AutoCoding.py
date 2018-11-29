# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 16:27:40 2018

@author: LIZY52
"""

for i in range(40, 390, 10):
    if i<100:
      print("'Value = %d " % i)
      print('LeftDoubleClick 1')
      print('Delay 500')
      print('KeyPress "Num %d", 1' % (i//10))
      print('KeyPress "Num 0", 1')
      '''
      print('KeyPress "Num %d", 1' % (i%10))
      '''
      print('Delay 500')
      print('')
      print("\'Send")
      print('')
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
      print('KeyPress "Num 0", 1')
      '''
      print('KeyPress "Num %d", 1' % (i%10))
      '''
      print('Delay 500')
      print('')
      print("\'Send")
      print('')
      print('KeyPress "Enter", 1')
      print('Delay 500')
      print('KeyPress "Enter", 1')
      print('Delay 5000')
      print('')