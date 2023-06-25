def single_number(nums):
  """
  Finds the single element in the array where every other element appears twice.
  Returns the element.
  """
  seen = set()
  for num in nums:
    if num in seen:
      seen.remove(num)
    else:
      seen.add(num)
  return seen.pop()

def main():
  nums = [2, 2, 1]
  print(single_number(nums))

if __name__ == "__main__":
  main()
