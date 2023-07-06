# Implement a function to calculate the square root of a given number.

def square_root(number, epsilon=1e-7):
    if number < 0:
        raise ValueError("Square root is undefined for negative numbers.")
    
    guess = number
    while abs(guess * guess - number) > epsilon:
        guess = (guess + number / guess) / 2
    
    return guess

# Example usage
input_number = 16
result = square_root(input_number)
print(f"The square root of {input_number} is: {result}")
