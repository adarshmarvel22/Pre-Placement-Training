# Implement a function to find the longest palindrome substring in a given string.


def longest_palindrome_substring(string):
    # Function to expand around the center for odd-length palindromes
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    # Initialize the longest palindrome substring
    longest_palindrome = ''

    # Iterate over each character in the string as the center of the palindrome
    for i in range(len(string)):
        # Check for odd-length palindrome
        odd_palindrome = expand_around_center(string, i, i)
        if len(odd_palindrome) > len(longest_palindrome):
            longest_palindrome = odd_palindrome

        # Check for even-length palindrome
        even_palindrome = expand_around_center(string, i, i + 1)
        if len(even_palindrome) > len(longest_palindrome):
            longest_palindrome = even_palindrome

    # Return the longest palindrome substring
    return longest_palindrome

# Test the function
input_string = input("Enter a string: ")
result = longest_palindrome_substring(input_string)
print("Longest palindrome substring:", result)
