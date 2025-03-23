my_list = []
for number in [10, 20, 30, 40]:
    my_list.append(number)
print(my_list)

my_list.insert(1, 15)
my_list.extend([50, 60, 70])
my_list.pop()
my_list.sort()
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
print("Final list:", my_list)