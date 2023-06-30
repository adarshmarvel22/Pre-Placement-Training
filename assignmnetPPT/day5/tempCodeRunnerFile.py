def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []
    
    original = []
    num_set = set(changed)
    
    for num in changed:
        if num // 2 in num_set:
            original.append(num // 2)
            num_set.remove(num // 2)
        elif num * 2 not in num_set:
            return []
    
    return original

changed = [1, 3, 4, 2, 6, 8]
original = findOriginalArray(changed)
print(original)
