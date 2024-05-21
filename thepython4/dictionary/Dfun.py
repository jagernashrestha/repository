#clear()
dictionary2 = {'jagerna':'6','shrestha':'8'}
dictionary2.clear()
print(dictionary2)
dictionary2['jagerna'] ='2'
print(dictionary2)
dictionary2 = {'jagerna':'','shrestha':'nana'}
del dictionary2['jagerna']
print(dictionary2)
dictionary2.fromkeys('jagerna')
print(dictionary2)
dictionary2.setdefault('shrestha')
print(dictionary2)