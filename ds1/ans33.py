# Write a Python program to remove duplicates from a list while preserving the order.

def remove_duplicates(lst):
    # Create an empty set to store unique elements
    unique_set = set()
    
    # Create a new list to store the elements in the original order
    new_lst = []
    
    # Iterate over each element in the list
    for elem in lst:
        # If the element is not already in the set, add it to the set
        # and append it to the new list
        if elem not in unique_set:
            unique_set.add(elem)
            new_lst.append(elem)
    
    # Return the new list without duplicates
    return new_lst

# Test the function
original_list = [1, 3, 2, 2, 1, 5, 4, 5, 4]
result = remove_duplicates(original_list)
print("List without duplicates:", result)
