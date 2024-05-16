import numpy as np

two_d_array = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,14,9]])
print(two_d_array)

print()

new_array = np.delete(two_d_array, 0 , axis=1)
print(new_array)