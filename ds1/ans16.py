# Implement a function to check if a given list is sorted in non-decreasing order.

def is_sorted(numbers):
    n = len(numbers)
    
    for i in range(n - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    
    return True

# Example usage
number_list = [1, 2, 3, 4, 5]
if is_sorted(number_list):
    print("The list is sorted in non-decreasing order.")
else:
    print("The list is not sorted in non-decreasing order.")
