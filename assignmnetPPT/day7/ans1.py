def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False

    s_dict = {}
    t_dict = {}

    for s_char, t_char in zip(s, t):
        if s_char not in s_dict and t_char not in t_dict:
            s_dict[s_char] = t_char
            t_dict[t_char] = s_char
        elif s_char in s_dict and s_dict[s_char] != t_char:
            return False
        elif t_char in t_dict and t_dict[t_char] != s_char:
            return False

    return True

s = "egg"
t = "add"
print(isomorphic_strings(s, t))  # Output: True
