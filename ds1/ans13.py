# Write a Python program to generate all permutations of a given string.


def generate_permutations(string):
    # Base case: If the string has only one character, return it as a single permutation
    if len(string) == 1:
        return [string]

    # Recursive case: Generate permutations for each character in the string
    permutations = []
    for i in range(len(string)):
        # Extract the current character
        current_char = string[i]
        
        # Generate permutations of the remaining characters
        remaining_chars = string[:i] + string[i+1:]
        remaining_permutations = generate_permutations(remaining_chars)
        
        # Append the current character to each permutation of the remaining characters
        for permutation in remaining_permutations:
            permutations.append(current_char + permutation)

    return permutations

# Example usage
input_string = "abc"
permutations = generate_permutations(input_string)
for permutation in permutations:
    print(permutation)
