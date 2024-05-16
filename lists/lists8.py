import numpy as np

my_array1 = np.array([1,2,3,4,5,6])
my_list1 = [1,2,3,4,5]

print(my_array1/2)
#print(my_list1/2) does not work

my_array2 = np.array([1,2,3,4,5,6, 'a'])
my_list2 = [1,2,3,4,5, 'a']

print(my_array2) #converts all elements to string
print(my_list2)