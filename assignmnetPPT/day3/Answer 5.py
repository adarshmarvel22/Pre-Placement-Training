def increment_integer(digits):
  """
  Increments the large integer represented by the array of digits.
  Returns the resulting array of digits.
  """
  carry = 1
  for i in range(len(digits) - 1, -1, -1):
    digit = digits[i] + carry
    if digit == 10:
      carry = 1
      digit = 0
    else:
      carry = 0
    digits[i] = digit
  if carry == 1:
    digits.insert(0, 1)
  return digits

def main():
  digits = [1, 2, 3]
  print(increment_integer(digits))

if __name__ == "__main__":
  main()
