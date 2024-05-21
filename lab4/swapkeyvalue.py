def swap1():
    old_dict ={ 'name':'jagerna','age':'shrestha'}
    new_dict = { }
    
    for key,value in old_dict.items():
        new_dict[value]= key
    print(new_dict)


