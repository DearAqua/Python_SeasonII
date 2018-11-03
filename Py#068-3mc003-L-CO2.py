# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:19:33 2018

@author: LIZY52
"""

def Mod_611_CO2_deal(coo,coo_bak):
    if coo >= coo_bak:
        if coo >= 1000:
            fan = 6
        elif coo >= 800:
            fan = 4
        elif coo >=550:
            fan = 3
        else:
            fan = 2
    else:
        if coo < 450:
            fan = 2
        elif coo < 700:
            fan = 3
        elif coo < 900:
            fan= 4
        else:
            fan = 6
    print(coo,'\t',fan) 
    
circle = 1    
coo_bak = 0   
while circle == 1:
    print('input CO2')
    coo = int(input())
    Mod_611_CO2_deal(coo,coo_bak)
    coo_bak = coo