# Implement a function to find the first non-repeating character in a string.

def find_first_non_repeating_char(string):
    char_count = {}

    # Count the occurrences of each character
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the first character with count 1
    for char in string:
        if char_count[char] == 1:
            return char

    # If no non-repeating character is found, return None
    return None

# Example usage
input_string = "abbcdeeff"
first_non_repeating = find_first_non_repeating_char(input_string)

if first_non_repeating is not None:
    print(f"The first non-repeating character is: {first_non_repeating}")
else:
    print("There is no non-repeating character.")
