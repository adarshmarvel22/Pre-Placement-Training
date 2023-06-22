def max_product_of_three(nums):
  """
  Finds the maximum product of three numbers in the array nums.

  Args:
    nums: The array of integers.

  Returns:
    The maximum product of three numbers.
  """

  max1 = nums[0]
  max2 = nums[1]
  max3 = nums[2]
  min1 = nums[0]
  min2 = nums[1]
  for num in nums:
    if num > max1:
      max3 = max2
      max2 = max1
      max1 = num
    elif num > max2:
      max3 = max2
      max2 = num
    elif num > min1:
      min2 = min1
      min1 = num
    elif num > min2:
      min2 = num
  return max(max1 * max2 * max3, min1 * min2)


def main():
  nums = [1, 2, 3]
  max_product = max_product_of_three(nums)
  print(max_product)


if __name__ == "__main__":
  main()
