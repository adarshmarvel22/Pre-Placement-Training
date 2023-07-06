# Write a Python program to sort a list of integers in ascending order.


def sort_list(lst):
    return sorted(lst)

# Test the function
input_list = input("Enter a list of integers (space-separated): ").split()
input_list = [int(num) for num in input_list]  # Convert the input to a list of integers
sorted_list = sort_list(input_list)
print("Sorted list:", sorted_list)
