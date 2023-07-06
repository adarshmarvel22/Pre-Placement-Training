# Implement a function to check if a given number is a power of two.

def is_power_of_two(number):
    if number <= 0:
        return False
    
    return (number & (number - 1)) == 0

# Example usage
input_number = 16
if is_power_of_two(input_number):
    print(f"{input_number} is a power of two.")
else:
    print(f"{input_number} is not a power of two.")
