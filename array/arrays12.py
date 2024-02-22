import numpy as np

two_d_array = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,14,9]])
print(two_d_array)

print()

def search_for_element(array, element):
    for index_row in range(len(array)):
        for index_col in range(len(array[0])):
            if(array[index_row][index_col] == element):
                return "The element " + str(element) + " is on the position (" + str(index_row) + "," + str(index_col) + ")"
    
    return "Element not found"

print(search_for_element(two_d_array, 55))