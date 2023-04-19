# Changing and Adding Elements in arrays

import array as arr

numbers = arr.array('i', [1,2,3,4,5,6,7])

numbers[0] = 0
print(numbers)

numbers[2:6] = arr.array('i', [10,11,12,13])
print(numbers)

numbers[6] = 20
print(numbers)

numbers.append(-10)
print(numbers)

numbers.extend([5, 6, 7])
print(numbers)