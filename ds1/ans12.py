# Implement a function to check if a given string is an anagram of another string.


def is_anagram(str1, str2):
    str1 = str1.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    str2 = str2.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    
    if len(str1) != len(str2):
        return False
    
    str1_counts = {}
    str2_counts = {}
    
    for char in str1:
        if char in str1_counts:
            str1_counts[char] += 1
        else:
            str1_counts[char] = 1
    
    for char in str2:
        if char in str2_counts:
            str2_counts[char] += 1
        else:
            str2_counts[char] = 1
    
    return str1_counts == str2_counts

# Example usage
string1 = "listen"
string2 = "silent"
if is_anagram(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
