# Write a program to check if a given number is a perfect square.

def is_perfect_square(num):
    # If the number is less than 0, it is not a perfect square
    if num < 0:
        return False

    # If the number is 0 or 1, it is a perfect square
    if num == 0 or num == 1:
        return True

    # Use binary search to find the square root of the number
    left = 1
    right = num

    while left <= right:
        mid = left + (right - left) // 2

        # If the middle number squared equals the input number, it is a perfect square
        if mid * mid == num:
            return True
        # If the square of the middle number is greater than the input number, search in the left half
        elif mid * mid > num:
            right = mid - 1
        # If the square of the middle number is smaller than the input number, search in the right half
        else:
            left = mid + 1

    # If the loop ends without finding the square root, the number is not a perfect square
    return False

# Test the function
number = int(input("Enter a number: "))
if is_perfect_square(number):
    print("The number is a perfect square.")
else:
    print("The number is not a perfect square.")
