# Write a Python program to find the intersection of two lists.

def find_intersection(list1, list2):
    intersection = []
    for element in list1:
        if element in list2:
            intersection.append(element)
    return intersection

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = find_intersection(list1, list2)
print(intersection)
