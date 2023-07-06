# Implement a function to check if a given string is a palindrome.

def is_palindrome(input_str):
    # Remove any spaces and convert to lowercase
    input_str = input_str.replace(" ", "").lower()
    
    # Compare the original string with its reverse
    return input_str == input_str[::-1]

# Test the function
string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
