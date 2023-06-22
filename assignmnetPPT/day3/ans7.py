def find_missing_ranges(nums, lower, upper):
  """
  Finds the shortest sorted list of ranges that covers all the missing numbers in the
  given range.
  Returns the list of ranges.
  """
  ranges = []
  current_range = [lower, lower]
  for num in nums:
    if num < current_range[1]:
      current_range[1] = num
    else:
      if current_range[1] - current_range[0] > 1:
        ranges.append(current_range)
      current_range = [num, num]
  if current_range[1] - current_range[0] > 1:
    ranges.append(current_range)
  ranges.append([upper, upper])
  ranges.sort()
  return ranges

def main():
  nums = [0, 1, 3, 50, 75]
  lower = 0
  upper = 99
  print(find_missing_ranges(nums, lower, upper))

if __name__ == "__main__":
  main()
