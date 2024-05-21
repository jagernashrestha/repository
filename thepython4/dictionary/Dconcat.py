##concationationof dictionary
d1 = {'k1':'1','k2':'2'}
d2 = {'k3':'1','k4':'2'}
d3 = {**d1,**d2}#
print(d3)
print(d1|d2)