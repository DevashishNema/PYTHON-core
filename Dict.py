my_dict = dict()
print(my_dict)
print(type(my_dict))
print(id(my_dict))
my_dict['name'] = 'Devashish'
print(my_dict)

my_dict['qualification'] = 'B.Tech'
print(my_dict)

my_dict['name'] = 'Deva'
print(my_dict)
print(id(my_dict))

my_dict['age'] = '23'
my_dict['t'] = 't'

# del my_dict['name']
# print(my_dict)
# my_dict.clear()
# print(my_dict)

# my_dict['name']
# print(my_dict)
my_dict['1'] = 'D'

print(len(my_dict))
print(max(my_dict))
print(my_dict.keys())
# print(my_dict(keys()))
print(my_dict.items())

# print(my_dict.get('name'))
# print(my_dict.get('key','D'))
print(my_dict.get('key'))

# print(my_dict['key'])

# my_dict.pop('key')

print(my_dict)

my_dict.pop('t')
# print(my_dict.pop('t'))
print(my_dict)

# my_dict.values()
# print(my_dict.values())

del my_dict['qualification']
print(my_dict)
my_dict.clear()
print(my_dict)

del my_dict
print(my_dict)

