def move_zeros(nums):
  """
  Moves all 0's to the end of the array while maintaining the relative order of the nonzero elements.

  Args:
    nums: The array of integers.

  Returns:
    The array with all 0's moved to the end.
  """

  count = 0
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[count] = nums[i]
      count += 1
  for i in range(count, len(nums)):
    nums[i] = 0


def main():
  nums = [0, 1, 0, 3, 12]
  move_zeros(nums)
  print(nums)


if __name__ == "__main__":
  main()