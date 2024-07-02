import sys

list = [1,2,3,4,5,6,4]
tuple = (5,6,7,2,9,8,2,1)
set = {10,20,30,50,80,90,70,60}

lsize = sys.getsizeof(list)


print(lsize )

import keyword
list = [1,2,3,4,5,6,4]

list = keyword.kwlist
print(list)
