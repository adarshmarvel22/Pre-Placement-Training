def can_plant_flowers(flowerbed, n):
  """
  Returns true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

  Args:
    flowerbed: The array of integers.
    n: The number of new flowers to plant.

  Returns:
    True if n new flowers can be planted, False otherwise.
  """

  count = 0
  for i in range(len(flowerbed)):
    if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 1) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 1):
      count += 1
  return count >= n


def main():
  flowerbed = [1, 0, 0, 0, 1]
  n = 1
  can_plant = can_plant_flowers(flowerbed, n)
  print(can_plant)


if __name__ == "__main__":
  main()
