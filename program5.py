# concatenation of  two arrays

import array as arr

odd = arr.array('i', [1,3,5,7])
even = arr.array('i', [2,4,6])

numbers = arr.array('i')
numbers = odd + even

print(numbers)

