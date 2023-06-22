def remove_element(nums, val):
  """
  Removes all occurrences of the given value from the array in-place.

  Args:
    nums: The array of integers.
    val: The value to remove.

  Returns:
    The number of elements in the array that are not equal to val.
  """

  i = 0
  j = 0
  while i < len(nums):
    if nums[i] != val:
      nums[j] = nums[i]
      j += 1
    i += 1
  return j

# Driver Code
if __name__ == "__main__":
    nums = [3,2,2,3]
    nums_size = 4
    val = 3
    ans = remove_element(nums, val)
    print(ans)