# Write a Python program to reverse a string without using any built-in string reversal functions.

def reverse_string(input_str):
    reversed_str = ''
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str

# Test the function
string = input("Enter a string: ")
reversed_string = reverse_string(string)
print("Reversed string:", reversed_string)
