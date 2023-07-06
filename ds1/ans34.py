# Implement a function to find the longest common prefix among a list of strings.

def longest_common_prefix(strings):
    # If the list is empty, return an empty string
    if not strings:
        return ""

    # Find the minimum length among all strings in the list
    min_length = min(len(string) for string in strings)

    # Initialize the common prefix variable
    common_prefix = ""

    # Iterate over the characters at each index up to the minimum length
    for i in range(min_length):
        # Get the character at index i of the first string
        char = strings[0][i]

        # Check if the character is common to all strings
        if all(string[i] == char for string in strings):
            # If it is common, append the character to the common prefix
            common_prefix += char
        else:
            # If it is not common, break the loop
            break

    # Return the common prefix
    return common_prefix

# Test the function
string_list = ["flower", "flow", "flight"]
result = longest_common_prefix(string_list)
print("Longest common prefix:", result)
