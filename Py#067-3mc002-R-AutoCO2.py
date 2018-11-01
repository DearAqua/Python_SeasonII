# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:32:21 2018

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

def Mod_611_CO2_deal(coo,coo_bak):
    if coo >= coo_bak:
        fan = Mod_611_CO2_up(coo)
    else:
        fan = Mod_611_CO2_down(coo)
    print(coo,'\t',fan) 

#    Initialize
coo = 0
coo_bak = 0    
circle = 1

#   input
print('Up-limit:')
var_u = int(input())
print('Down-limit:')
var_d = int(input())
print('tolerance')
var_t = int(input())

circleup = 1
circledown = 1

var_bak = var_d
print('CO2浓度\t风挡') 

while circleup == 1:  
    if var_bak < var_u:
        coo = var_bak
        Mod_611_CO2_deal(coo,coo_bak)
        coo_bak = coo
    else:
        circleup = 0
    var_bak = var_bak + var_t
    
var_bak = var_u      
while circledown == 1:
    if var_bak > var_d:
        coo = var_bak
        Mod_611_CO2_deal(coo,coo_bak)
        coo_bak = coo
    else:
        circledown = 0
    var_bak = var_bak - var_t