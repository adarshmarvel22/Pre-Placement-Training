# Write a program to find the number of occurrences of a given element in a list.

def count_occurrences(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count += 1

    return count

# Test the function
number_list = [1, 2, 3, 4, 2, 2, 5, 2]
element = 2
occurrences = count_occurrences(number_list, element)
print("Number of occurrences:", occurrences)
