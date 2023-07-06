# Implement a function to find the sum of all numbers in a list.



def find_sum(lst):
    return sum(lst)

# Test the function
input_list = input("Enter a list of numbers (space-separated): ").split()
input_list = [int(num) for num in input_list]  # Convert the input to a list of integers
sum_of_numbers = find_sum(input_list)
print("Sum of numbers:", sum_of_numbers)
