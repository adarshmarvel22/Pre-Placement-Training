# Implement a function to find the maximum subarray sum in a given list.

def find_max_subarray_sum(numbers):
    if not numbers:
        return 0
    
    max_sum = current_sum = numbers[0]
    
    for num in numbers[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage
number_list = [1, -3, 2, 1, -1, 4, -2]
max_sum = find_max_subarray_sum(number_list)
print(f"The maximum subarray sum is: {max_sum}")
