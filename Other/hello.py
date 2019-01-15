
print("Hello!")

import os
dir = os.listdir()

print(dir)

a = ['a', 'b', 'c']
b = [1, 2, 3]

for i,j in zip(a,b):
    print("%s is %s" % (i, j))
