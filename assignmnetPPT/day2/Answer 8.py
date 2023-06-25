def min_score(nums, k):
  """
  Finds the minimum score of nums after applying the mentioned operation at most once for each index in it.

  Args:
    nums: The array of integers.
    k: The maximum value of x.

  Returns:
    The minimum score of nums.
  """

  min_val = nums[0]
  max_val = nums[0]
  for i in range(1, len(nums)):
    min_val = min(min_val, nums[i] - k)
    max_val = max(max_val, nums[i] + k)
  return max_val - min_val


def main():
  nums = [1]
  k = 0
  min_score_result = min_score(nums, k)
  print(min_score_result)


if __name__ == "__main__":
  main()
