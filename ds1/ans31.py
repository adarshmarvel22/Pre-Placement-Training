# Write a program to find the sum of all even numbers in a list.

def sum_of_even_numbers(numbers):
    # Initialize the sum variable
    total_sum = 0

    # Iterate over each number in the list
    for num in numbers:
        # Check if the number is even
        if num % 2 == 0:
            # Add the even number to the sum
            total_sum += num

    # Return the sum of even numbers
    return total_sum

# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(numbers)
print("Sum of even numbers:", result)
