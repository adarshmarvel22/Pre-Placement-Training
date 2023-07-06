# Implement a function to calculate the power of a number using recursion.

def power(base, exponent):
    # Base case: if the exponent is 0, return 1
    if exponent == 0:
        return 1
    # Recursive case: calculate the power using recursion
    else:
        return base * power(base, exponent - 1)

# Test the function
base = 2
exponent = 5
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is:", result)
