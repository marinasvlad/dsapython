import numpy as np

two_d_array = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,14,0]])

new_two_array = np.insert(two_d_array, 0, [[1,2,3,4]], axis=0)
print(new_two_array)

print()

new_three_array = np.append(two_d_array, [[1,2,3,4]], axis=0)
print(new_three_array)