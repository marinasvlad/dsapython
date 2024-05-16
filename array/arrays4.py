from array import *

arr1 = array('i', [1,2,3,4,5,6])

print(arr1)

def access_element(array, index):
    if(index >= len(array)):
        print('There is not any element for that idnex')
    else:
        print(array[index])

access_element(arr1, 6)