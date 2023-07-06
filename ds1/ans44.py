# Implement a function to check if a given number is a perfect number.

def is_perfect_number(number):
    # Check if the number is positive
    if number <= 0:
        return False

    # Find the divisors of the number and sum them
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)

    # Check if the sum of divisors is equal to the number
    return divisors_sum == number

# Test the function
input_number = int(input("Enter a number: "))
if is_perfect_number(input_number):
    print("The number is a perfect number.")
else:
    print("The number is not a perfect number.")
