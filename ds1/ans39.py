# Write a program to find the sum of digits of a given number.

def sum_of_digits(number):
    # Convert the number to a string
    number_str = str(number)

    # Initialize the sum variable
    digit_sum = 0

    # Iterate over each character in the string
    for digit in number_str:
        # Convert the character back to an integer and add it to the sum
        digit_sum += int(digit)

    # Return the sum of digits
    return digit_sum

# Test the function
input_number = int(input("Enter a number: "))
result = sum_of_digits(input_number)
print("Sum of digits:", result)
