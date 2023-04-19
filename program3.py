# Convert list into Arrays and use Slicing on ARRAYS

import array as arr

numbers_list = [3,87,6,17,90,5,-7,88,9]
numbers_array = arr.array('i', numbers_list)

print(numbers_array[2:5])
print(numbers_array[:-5])
print(numbers_array[5:])
print(numbers_array[:])