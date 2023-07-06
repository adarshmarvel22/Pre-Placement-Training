# Write a program to calculate the factorial of a given number.


def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Test the function
number = int(input("Enter a number: "))
factorial_result = factorial(number)
if factorial_result is None:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", number, "is:", factorial_result)
