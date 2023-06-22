def longest_harmonious_subsequence(nums):
  """
  Finds the length of the longest harmonious subsequence in the array nums.

  Args:
    nums: The array of integers.

  Returns:
    The length of the longest harmonious subsequence.
  """

  max_value = nums[0]
  min_value = nums[0]
  max_len = 1
  for num in nums:
    if num > max_value:
      max_value = num
    elif num < min_value:
      min_value = num
    if num == max_value - 1 or num == min_value + 1:
      max_len += 1
  return max_len


def main():
  nums = [1, 3, 2, 2, 5, 2, 3, 7]
  longest_len = longest_harmonious_subsequence(nums)
  print(longest_len)


if __name__ == "__main__":
  main()
