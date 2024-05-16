my_dict = {'name': 'Edy', 'age': 26, 'address' :'London'}

def search_dict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key,value
    return 'The value does not exist'

print(search_dict(my_dict, 28))
