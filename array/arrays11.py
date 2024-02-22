import numpy as np

two_d_array = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,14,9]])
print(two_d_array)

print()

def transverse_2d_array(array):
    for index_row in range(len(array)):
        for index_col in range(len(array[0])):
            print(array[index_row][index_col], end=" ")
        print()

transverse_2d_array(two_d_array)