def three_sum_closest(nums, target):
  """
  Finds three integers in nums such that the sum is closest to the target.
  Returns the sum of the three integers.
  """
  nums.sort()
  closest_sum = float("inf")
  for i in range(len(nums)):
    left = i + 1
    right = len(nums) - 1
    while left < right:
      sum = nums[i] + nums[left] + nums[right]
      if abs(sum - target) < abs(closest_sum - target):
        closest_sum = sum
      if sum < target:
        left += 1
      elif sum > target:
        right -= 1
      else:
        return sum
  return closest_sum

def main():
  nums = [-1, 2, 1, -4]
  target = 1
  print(three_sum_closest(nums, target))

if __name__ == "__main__":
  main()
