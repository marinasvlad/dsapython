my_dict = {'name': 'Edy', 'age': 26, 'address' :'London'}

def transverse_dict(dict):
    for key in dict:
        print(key, dict[key])

transverse_dict(my_dict)