
import array

arr1 = array.array('i', [1, 2, 3, 4, 5, 6])

def transverse(array):
    for element in array:
        print(element, end=' ')

transverse(arr1)
print()
def access(array, index):
    if index > len(array):
        print('Index out of range')
    else:
        print(array[index])

access(arr1, 1)
access(arr1, 50)
print()

arr1.append(10)
print(arr1)
print()

arr1.insert(0, 15)
print(arr1)
print()

arr1.extend([100, 200, 300])
print(arr1)
print()

arr1.fromlist([150, 250])
print(arr1)
print()

arr1.remove(15)
print(arr1)
print()

arr1.pop()
print(arr1)
print()

print(arr1.index(200))
print()

arr1.reverse()
print(arr1)
print()

print(arr1.buffer_info())
print()


print(arr1.count(3))


print(arr1.tobytes())

print(arr1.tolist())

print(arr1[2:4])