def canSwapString(s, goal):
    if len(s) != len(goal):
        return False

    differences = []
    indices = []

    for i, c in enumerate(s):
        if c != goal[i]:
            differences.append(c)
            indices.append(i)

    if len(differences) != 2:
        return False

    i, j = indices
    return s[i] == goal[j] and s[j] == goal[i]


# Test the function with the provided example
s = "ab"
goal = "ba"
result = canSwapString(s, goal)
print(result)  # Output: True
