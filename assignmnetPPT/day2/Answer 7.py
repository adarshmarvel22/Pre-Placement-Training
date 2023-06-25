def is_monotonic(nums):
  """
  Checks if the array nums is monotonic.

  Args:
    nums: The array of integers.

  Returns:
    True if the array is monotonic, False otherwise.
  """

  increasing = True
  decreasing = True
  for i in range(1, len(nums)):
    if nums[i] < nums[i - 1]:
      increasing = False
    elif nums[i] > nums[i - 1]:
      decreasing = False
  return increasing or decreasing


def main():
  nums = [1, 2, 2, 3]
  is_monotonic_result = is_monotonic(nums)
  print(is_monotonic_result)


if __name__ == "__main__":
  main()
