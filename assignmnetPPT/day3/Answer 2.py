def four_sum(nums, target):
  """
  Finds all the quadruplets in nums whose sum is equal to the target.
  Returns a list of the quadruplets.
  """
  quadruplets = []
  nums.sort()
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      left = j + 1
      right = len(nums) - 1
      while left < right:
        sum = nums[i] + nums[j] + nums[left] + nums[right]
        if sum == target:
          quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
          left += 1
          right -= 1
        elif sum < target:
          left += 1
        else:
          right -= 1
  return quadruplets

def main():
  nums = [1, 0, -1, 0, -2, 2]
  target = 0
  print(four_sum(nums, target))

if __name__ == "__main__":
  main()
