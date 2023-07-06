# Implement a function to count the occurrence of each element in a list.


def count_occurrences(lst):
    occurrence_count = {}
    for item in lst:
        if item in occurrence_count:
            occurrence_count[item] += 1
        else:
            occurrence_count[item] = 1
    return occurrence_count

# Test the function
input_list = input("Enter a list of elements (space-separated): ").split()
occurrence_dict = count_occurrences(input_list)
print("Occurrences:")
for item, count in occurrence_dict.items():
    print(f"{item}: {count}")
