''' Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
The array length may be less than 4.

 '''

def array_front9(nums):
  return nums[:4].count(9) > 0