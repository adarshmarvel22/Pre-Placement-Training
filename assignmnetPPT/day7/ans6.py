def rotateString(s, goal):
    if len(s) != len(goal):
        return False

    s_double = s + s
    if goal in s_double:
        return True
    else:
        return False

s = "abcde"
goal = "cdeab"
print(rotateString(s, goal))  # Output: True
