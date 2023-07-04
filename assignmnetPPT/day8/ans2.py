def isValid(s):
    stack = []

    for c in s:
        if c == '(' or c == '*':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False
            if stack[-1] == '(':
                stack.pop()
            elif stack[-1] == '*':
                stack.pop()
                if stack and stack[-1] == '(':
                    stack.pop()

    while stack and stack[-1] == '(':
        if len(stack) < 2:
            return False
        stack.pop()
        stack.pop()

    return not stack
s = "()"
result = isValid(s)
print(result)  # Output: True
