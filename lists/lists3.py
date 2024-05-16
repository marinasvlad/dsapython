my_list = ['a', 'b', 'c', 'd', 'e', 'f']

print(my_list[:2])

print(my_list[:])

print(my_list[1:])

my_list[0:2] = ['x', 'y']
print(my_list[:])

my_list.pop(3)

print(my_list)

my_list.pop()

print(my_list)

del my_list[1]

print(my_list)
my_list2 = ['a', 'b', 'c', 'd', 'e', 'f']

del my_list2[1:3]

print(my_list2)

my_list2.remove('a')

print(my_list2)