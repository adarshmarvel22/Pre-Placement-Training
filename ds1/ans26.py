# Implement a function to find the mode of a list of numbers.

from collections import Counter

def find_mode(numbers):
    count = Counter(numbers)
    mode = count.most_common(1)[0][0]
    return mode

# Example usage
number_list = [1, 2, 3, 4, 2, 2, 3, 4, 4, 4]
mode_value = find_mode(number_list)
print(f"The mode is: {mode_value}")
