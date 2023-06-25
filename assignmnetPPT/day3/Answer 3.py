def next_permutation(nums):
  """
  Finds the next permutation of nums.
  The replacement must be in place and use only constant extra memory.
  """
  i = len(nums) - 1
  while i > 0 and nums[i - 1] >= nums[i]:
    i -= 1
  if i == 0:
    nums.reverse()
    return
  j = len(nums) - 1
  while j > i and nums[j] <= nums[i - 1]:
    j -= 1
  nums[i - 1], nums[j] = nums[j], nums[i - 1]
  nums[i:] = nums[i:][::-1]
  return nums

def main():
  nums = [1, 2, 3]
  print(next_permutation(nums))

if __name__ == "__main__":
  main()
