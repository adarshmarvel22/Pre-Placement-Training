def max_pair_sum(nums):
  """
  Finds the maximum sum of min(ai, bi) for all i in the array nums.

  Args:
    nums: The array of integers.

  Returns:
    The maximum sum.
  """

  nums.sort()
  sum = 0
  for i in range(0, len(nums), 2):
    sum += nums[i]
  return sum


def main():
  nums = [1, 4, 3, 2]
  max_sum = max_pair_sum(nums)
  print(max_sum)


if __name__ == "__main__":
  main()