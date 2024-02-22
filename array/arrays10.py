import numpy as np

two_d_array = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,14,9]])
print(two_d_array)

print()

def access_element(array, row_index, col_index):
    if row_index >= len(array) or col_index >= len(array[0]):
        print("Incorrect index")
    else:
        print(array[row_index][col_index])

access_element(two_d_array, 1, 2)