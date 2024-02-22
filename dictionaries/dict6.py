my_dict = {'name': 'Edy', 'age': 26, 'address' :'London', 'education': 'master'}

print(my_dict)

my_dict.clear()
print(my_dict)

my_dict2 = {'name': 'Edy', 'age': 26, 'address' :'London', 'education': 'master'}

my_dict3 = my_dict2.copy()
print(my_dict3)


new_dict = {}.fromkeys([1,2,3], 0)
print(new_dict)

print(my_dict2.get('age'))

print(my_dict2.items())



