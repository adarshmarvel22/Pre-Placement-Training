def contains_duplicate(nums):
  """
  Returns true if any value appears at least twice in the array, and false if every element is distinct.

  Args:
    nums: The array of integers.

  Returns:
    True if the array contains duplicates, False otherwise.
  """

  seen = set()
  for num in nums:
    if num in seen:
      return True
    else:
      seen.add(num)
  return False


def main():
  nums = [1, 2, 3, 1]
  print(contains_duplicate(nums))


if __name__ == "__main__":
  main()
