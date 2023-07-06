# Write a Python program to check if a given string is a valid palindrome ignoring non-alphanumeric characters.

import re

def is_valid_palindrome(string):
    # Remove non-alphanumeric characters from the string
    alphanumeric_string = re.sub('[^a-zA-Z0-9]', '', string)
    
    # Convert the string to lowercase for case-insensitive comparison
    alphanumeric_string = alphanumeric_string.lower()
    
    # Check if the alphanumeric string is equal to its reverse
    return alphanumeric_string == alphanumeric_string[::-1]

# Test the function
input_string = input("Enter a string: ")
if is_valid_palindrome(input_string):
    print("The string is a valid palindrome.")
else:
    print("The string is not a valid palindrome.")
