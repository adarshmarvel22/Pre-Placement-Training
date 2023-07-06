# Write a Python program to remove all duplicates from a string.

def remove_duplicates(string):
    # Create an empty set to store unique characters
    unique_chars = set()

    # Create a new string to store the characters without duplicates
    new_string = ""

    # Iterate over each character in the string
    for char in string:
        # Check if the character is not in the set
        if char not in unique_chars:
            # Add the character to the set and append it to the new string
            unique_chars.add(char)
            new_string += char

    # Return the new string without duplicates
    return new_string

# Test the function
input_string = input("Enter a string: ")
result = remove_duplicates(input_string)
print("String without duplicates:", result)
