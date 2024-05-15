import array

my_array1 = array.array('i', [1, 2, 3, 4])

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return 1
    return -1

print(linear_search(my_array1, 2))

print(linear_search(my_array1, 20))