def search_insert(nums, target):
  """
  Searches for the target value in the array and returns its index.

  Args:
    nums: The sorted array of integers.
    target: The target value.

  Returns:
    The index of the target value, or the index where it would be if it were inserted in order.
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
  return low


def main():
  nums = [1, 3, 5, 6]
  target = 5
  index = search_insert(nums, target)
  print(index)


if __name__ == "__main__":
  main()