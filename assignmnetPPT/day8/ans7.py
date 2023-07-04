def decodeString(s: str) -> str:
    stack = []
    for c in range(len(s)):
        if s[c] != ']':
            stack.append(s[c])
        else:
            string = ''
            num = ''
            while stack[-1] != '[':
                string = stack.pop() + string
            stack.pop()
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            stack.append(int(num) * string)
            # print(num)
    return "".join(stack)  # Reverse the order of characters in the stack


# Test the function with the provided example
s = "3[a]2[bc]"
result = decodeString(s)
print(result)  # Output: "aaabcbc"
