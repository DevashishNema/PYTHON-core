list = [2,3,4,5,6,7,8,9,7]
tuple = (7,89,5,4,89,55,2,4,6,8,5)
set = {4,5,6,9,3,7,8,2,1}
dict = {'name':'devashish','qualification':'btech'}

x = frozenset(list)
y = frozenset(tuple)
z = frozenset(set)
p = frozenset(dict)

print(x)
print(y)
print(z)
print(p)

print(len(x))
print(max(x))
print(min(x))
print(sum(x))



x.symmetric_difference(y)
print(x.symmetric_difference(y))
