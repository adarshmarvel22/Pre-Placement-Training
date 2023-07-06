# Write a program to find the largest element in a given list.

def find_largest_element(lst):
    if not lst:
        return None

    largest_element = lst[0]
    for num in lst:
        if num > largest_element:
            largest_element = num

    return largest_element

# Test the function
input_list = input("Enter a list of numbers (space-separated): ").split()
input_list = [int(num) for num in input_list]  # Convert the input to a list of integers
largest = find_largest_element(input_list)
print("The largest element is:", largest)
