# use remove() and pop() to remove Array elements

import array as arr

numbers = arr.array('i', [0,1,2,3,4,5,6,7])

numbers.remove(6)
print(numbers)

print(numbers.pop(3))
print(numbers)

print(numbers.pop(-1))
print(numbers)