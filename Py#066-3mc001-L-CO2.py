# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:22:20 2018

@author: LIZY52
"""

def Mod_611_CO2_up(coo_in):
    if coo_in >= 1000:
        fan_out = 6
    elif coo_in >= 800:
        fan_out = 4
    elif coo_in >=550:
        fan_out = 3
    else:
        fan_out = 2
    return(fan_out)

def Mod_611_CO2_down(coo_in):
    if coo_in < 450:
        fan_out = 2
    elif coo_in < 700:
        fan_out = 3
    elif coo_in < 900:
        fan_out = 4
    else:
        fan_out = 6
    return(fan_out)

# Initialize
coo = 0
coo_bak = 0    
circle = 1

while circle == 1:
        print('输入当前CO2浓度')
        coo = int(input())
        if coo >= coo_bak:
            fan = Mod_611_CO2_up(coo)
        else:
            fan = Mod_611_CO2_down(coo)
        print(fan)
        coo_bak = coo