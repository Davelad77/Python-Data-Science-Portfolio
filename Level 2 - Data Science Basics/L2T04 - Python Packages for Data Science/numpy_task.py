'''
# Why does the below code line not create a 2d array?
# np.array((1, 0, 0), (0, 1, 0), (0, 0, 1, dtype=float)

# the code does not produce a 2d array as there are three tuples in the array
# the values of an array should be contained in square brackets which in turn should all be contained in parentheses
# the dtype=float should come after the closing square parenthesis of the array but inside the final closing parenthesis
# the correct code should be as follows

import numpy as np
example_array = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)], dtype=float)
print(example_array)


# what is the difference between the following two arrays?

a = np.array([0, 0, 0]) 
print(a)

b = np.array([[0, 0, 0]])
print(b)

# the difference between the two arrays is that the first array is a 1d array while the second array is a strangely nested 2d array
'''

# create a 3d array with values ranging from 1 to 48
import numpy as np
arr = np.linspace(1, 48, 48).reshape(3, 4, 4)
print(arr)
print()


# Index or slice this array to obtain the following:
# 20.0
print(arr[1, 0, 3])
print()

# Index or slice this array to obtain the following:
# [ 9. 10. 11. 12.]
print(arr[0, 2])
print()

# Index or slice this array to obtain the following:
# [[33. 34. 35. 36.] [37. 38. 39. 40.] [41. 42. 43. 44.] [45. 46. 47. 48.]]
print(arr[2])
print()

# Index or slice this array to obtain the following:
# [[5. 6.], [21. 22.] [37. 38.]]
print(arr[0:3, 1, 0:2])
print()

# Index or slice this array to obtain the following:
# [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]
rev_array = arr[: : -1]
last_two_rev_array = rev_array[0,0:4,2:4]
print(last_two_rev_array[:,: : -1 ])
print()

# Index or slice this array to obtain the following:
# [[13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]
first_num_array = arr[0:3, 0:4, 0]
print(first_num_array[:,: : -1])
print()

# Index or slice this array to obtain the following:
# [[1. 4.] [45. 48.]]
first_last_array = ([arr[0,0,0].item(),arr[0,0,3].item()],[arr[2,3,0].item(),arr[2,3,3].item()])
print(first_last_array)
print()

# Index or slice this array to obtain the following:
# [[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], [37. 38. 39. 40.]]
middle_array = np.vstack((arr[1,2:,],arr[2,0:2,]))
print(middle_array)
print()
