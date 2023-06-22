def find_error_nums(nums):
  """
  Finds the number that occurs twice and the number that is missing in the array.

  Args:
    nums: The array of integers.

  Returns:
    The array of the two numbers.
  """

  seen = set()
  duplicate = -1
  missing = -1
  for num in nums:
    if num in seen:
      duplicate = num
    else:
      seen.add(num)
  for i in range(1, len(nums) + 1):
    if i not in seen:
      missing = i
  return [duplicate, missing]


def main():
  nums = [1, 2, 2, 4]
  error_nums = find_error_nums(nums)
  print(error_nums)


if __name__ == "__main__":
  main()
