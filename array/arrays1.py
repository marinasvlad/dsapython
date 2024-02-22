import array

my_array = array.array('i') # space complexity is O(1)
print(my_array)
my_array1 = array.array('i', [1,2,3,4]) # space complexity is O(n)
print(my_array1)

import numpy as np

np_array = np.array([], dtype=int) # space complexity is O(1)
print(np_array)

np_array1 = np.array([1,2,3,4])  # space complexity is O(n)
print(np_array1)