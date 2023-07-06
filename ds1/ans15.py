# Write a program to find the median of a list of numbers.

def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 0:
        # If the number of elements is even, the median is the average of the middle two elements
        middle_index_1 = n // 2 - 1
        middle_index_2 = n // 2
        median = (sorted_numbers[middle_index_1] + sorted_numbers[middle_index_2]) / 2
    else:
        # If the number of elements is odd, the median is the middle element
        middle_index = n // 2
        median = sorted_numbers[middle_index]
    
    return median

# Example usage
number_list = [5, 2, 9, 1, 7, 6, 3]
median_value = find_median(number_list)
print(f"The median is: {median_value}")
