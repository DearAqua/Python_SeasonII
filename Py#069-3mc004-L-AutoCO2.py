#    Initialize
coo = 0
coo_bak = 0    
circle = 1

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
