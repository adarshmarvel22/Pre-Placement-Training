def increment_integer(digits):
  """
  Increments the large integer represented by the array of digits and returns the resulting array of digits.

  Args:
    digits: The array of digits representing the integer.

  Returns:
    The array of digits representing the incremented integer.
  """

  carry = 1
  for i in range(len(digits) - 1, -1, -1):
    digits[i] += carry
    if digits[i] == 10:
      digits[i] = 0
      carry = 1
    else:
      carry = 0
  if carry == 1:
    digits.insert(0, 1)
  return digits


def main():
  digits = [1, 2, 3]
  incremented_digits = increment_integer(digits)
  print(incremented_digits)


if __name__ == "__main__":
  main()
