from array import *

# 1 create an array and transverse it

arr1 = array('i', [1,2,3,4,5])

for element in arr1:
    print(element, end= " ")
print()
# 2 access individual elements through indexes
    
print(arr1[2])
print(arr1[0])
print(arr1[4])

# 3 append any value to the array using append()

arr1.append(10)
print(arr1)

# 4 insert a value in the array using insert()

arr1.insert(0,15)
print(arr1)

# 5 extend the array using extend()

arr1.extend(array('i', [8,9,12]))
print(arr1)

# 6 add items from list into array using fromlist()

my_list = list([20,21,22])

arr1.fromlist(my_list)
print(arr1)

# 7 remove any element using remove()

arr1.remove(5)
print(arr1)

# 8 remove last element of the array using pop()

arr1.pop()
print(arr1)

# fetch any element from the array using fetch()

print(arr1.index(20))

# 10 reverse a python array using reverse()

arr1.reverse()
print(arr1)

# 11 get array buffe information through buffer_info

print(arr1.buffer_info())

# 12 check the nr of occurances of an element using count()

print(arr1.count(2))

# 13 convert array to list using tolist()

print(arr1.tolist())

# 14 slice elements from the array

print(arr1[4:8])
