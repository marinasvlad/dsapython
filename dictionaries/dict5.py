my_dict = {'name': 'Edy', 'age': 26, 'address' :'London'}


del my_dict['age']

print(my_dict)

removed_element = my_dict.pop('name')

print(removed_element)
print(my_dict)

my_dict.clear()
print(my_dict)