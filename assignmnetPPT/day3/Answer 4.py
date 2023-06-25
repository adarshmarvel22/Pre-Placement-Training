def binary_search(nums, target):
  """
  Finds the index of the target value in the sorted array nums.
  Returns -1 if the target value is not found.
  """
  low = 0
  high = len(nums) - 1
  while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1

def main():
  nums = [1, 3, 5, 6]
  target = 5
  print(binary_search(nums, target))

if __name__ == "__main__":
  main()
