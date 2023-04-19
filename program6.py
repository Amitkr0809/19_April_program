# WAP to Remove Python Array Elements

import array as arr

number = arr.array('i', [11,22,33,44,55,66,77,88])

del number[2]
print(number)

del number[3:6]
print(number)

del number[-1]
print(number)

