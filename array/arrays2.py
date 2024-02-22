import array

my_array1 = array.array('i', [1,2,3,4])
print(my_array1)

my_array1.insert(0, 6) # O(n) time complexity, O(1) space complexity

print(my_array1)
