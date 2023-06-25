def binary_search(nums, target):
  """
  Searches for target in the array nums.

  Args:
    nums: The array of integers.
    target: The integer to search for.

  Returns:
    The index of target in nums, if it exists. Otherwise, -1.
  """

  low = 0
  high = len(nums) - 1
  while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1


def main():
  nums = [-1, 0, 3, 5, 9, 12]
  target = 9
  index = binary_search(nums, target)
  print(index)


if __name__ == "__main__":
  main()
