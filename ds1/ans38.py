# Implement a function to find the missing number in a given list of consecutive numbers.

def find_missing_number(numbers):
    # Calculate the expected sum of consecutive numbers
    expected_sum = (len(numbers) + 1) * (numbers[0] + numbers[-1]) // 2

    # Calculate the actual sum of the given numbers
    actual_sum = sum(numbers)

    # Calculate the missing number
    missing_number = expected_sum - actual_sum

    # Return the missing number
    return missing_number

# Test the function
number_list = [1, 2, 3, 5, 6]
missing_number = find_missing_number(number_list)
print("Missing number:", missing_number)
