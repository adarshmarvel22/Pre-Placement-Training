# Implement a function to check if a given string is a valid palindrome considering case sensitivity.

def is_valid_palindrome(string):
    # Remove spaces and punctuation from the string and convert it to lowercase
    cleaned_string = ''.join(e for e in string if e.isalnum()).lower()

    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Test the function
input_string = input("Enter a string: ")
if is_valid_palindrome(input_string):
    print("The string is a valid palindrome.")
else:
    print("The string is not a valid palindrome.")
