my_array = [5,3,2,1,1,2,3,4]

def remove_duplicates(arr):
    for element in arr:
        if arr.count(element) > 1:
            arr.remove(element)
    return arr

print(remove_duplicates(my_array))