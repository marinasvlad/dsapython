from array import *

arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d', [1.3, 1.5, 1.6])

print(arr1)

def transverse_array(array): #time complexity O(n), space complexity O(1)
    for i in array:
        print(i, end= " ")

transverse_array(arr1)