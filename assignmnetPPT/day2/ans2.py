import collections

def max_types(candyType):
  """
  Finds the maximum number of different types of candies Alice can eat if she only eats n / 2 of them.

  Args:
    candyType: The array of candy types.

  Returns:
    The maximum number of different types of candies.
  """

  count = collections.Counter(candyType)
  max_types = 0
  for candy_type, count in count.items():
    if count > max_types:
      max_types = count
  return max_types


def main():
  candyType = [1, 1, 2, 2, 3, 3]
  max_types = max_types(candyType)
  print(max_types)


if __name__ == "__main__":
  main()
