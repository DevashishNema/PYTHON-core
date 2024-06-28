my_set = {10,20,50,60,80,20}
# print(my_set)

# print(len(my_set))
# print(max(my_set))
# print(min(my_set))
# print(list(my_set))

my_set.add(60)
print(my_set)

list = [10,50,60,30,20,80,90,100]

my_set.update(list)
print(my_set)

# my_set.remove(80)
# print(my_set)
my_set.discard(80)
print(my_set)

my_set.union(list)
print(my_set.union(list))

my_set.intersection(list)
print(my_set.intersection(list))

my_set.difference(list)
print(my_set.difference(list))
