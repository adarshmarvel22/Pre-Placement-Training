# Implement a function to remove duplicate elements from a list.


def remove_duplicates(lst):
    return list(set(lst))

# Test the function
input_list = input("Enter a list of elements (space-separated): ").split()
unique_list = remove_duplicates(input_list)
print("List with duplicates removed:", unique_list)
