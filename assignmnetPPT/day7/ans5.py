def reverseStr(s, k):
    chars = list(s)
    n = len(chars)

    for i in range(0, n, 2 * k):
        start = i
        end = min(i + k, n)  # Handle case when remaining characters are less than k
        chars[start:end] = reversed(chars[start:end])

    return ''.join(chars)

s = "abcdefg"
k = 2
print(reverseStr(s, k))  # Output: "bacdfeg"
