a = [1,2,3]
b = [4,5,6]

c = a + b
print(c)

x = [0]
y = x * 4
print(y)

xx = [0,1]
yy = 4 * xx

print(yy)

print(len(b))
print(max(b))
print(min(b))

print(sum(a))


my_list = []

while(True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    my_list.append(value)
    average = sum(my_list) / len(my_list)

print('Average ', average)
