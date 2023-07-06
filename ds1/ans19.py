# Write a program to remove all vowels from a given string.

def remove_vowels(string):
    vowels = "aeiouAEIOU"
    without_vowels = ""
    
    for char in string:
        if char not in vowels:
            without_vowels += char
    
    return without_vowels

# Example usage
input_string = "Hello, World!"
result = remove_vowels(input_string)
print(result)
