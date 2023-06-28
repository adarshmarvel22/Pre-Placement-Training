def plusOne(digits):
    n = len(digits)

    # Iterate through the digits from right to left
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            # If the current digit is less than 9, increment it and return the digits
            digits[i] += 1
            return digits
        else:
            # If the current digit is 9, set it to 0 and continue to the next digit
            digits[i] = 0

    # If all digits are 9, we need an additional digit at the beginning
    digits.insert(0, 1)
    return digits


# Driver code
digits = [1, 2, 3]
result = plusOne(digits)
print(result)
