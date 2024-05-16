list1 = 'spam'
list2 = list(list1)
print(list2)

list3 = 'spam spam spam'
list4 = list3.split()
print(list4)

list5 = 'spam-spam-spam'
list6 = list5.split('-')
print(list6)

list7 = ['ce','mai','faci', '?']
print(list7)
print(' '.join(list7))