# Write a Python program to find the second largest number in a list.

def find_second_largest(lst):
    if len(lst) < 2:
        return None

    largest = max(lst[0], lst[1])
    second_largest = min(lst[0], lst[1])

    for i in range(2, len(lst)):
        if lst[i] > largest:
            second_largest = largest
            largest = lst[i]
        elif lst[i] > second_largest and lst[i] != largest:
            second_largest = lst[i]

    return second_largest

# Test the function
input_list = input("Enter a list of numbers (space-separated): ").split()
input_list = [int(num) for num in input_list]  # Convert the input to a list of integers
second_largest = find_second_largest(input_list)
if second_largest is None:
    print("There is no second largest element in the list.")
else:
    print("The second largest element is:", second_largest)
