from collections import Counter

def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []
    
    original = []
    hashmap = {}

    # Create a hashmap with the frequency of elements
    hashmap = Counter(changed)
    
    changed.sort()
    n = len(changed)//2

    for i in range(n):
        if changed[i] * 2 in hashmap:

            hashmap[changed[i] * 2] =-1
            hashmap[changed[i]] =-1

            original.append(changed[i])

            if hashmap[changed[i] * 2] == 0:
                hashmap.pop(changed[i] * 2)

            if hashmap[changed[i]] == 0:
                hashmap.pop(changed[i])
        # else : 
            # return []
    
    return original

changed = [1, 3, 4, 2, 6, 8]
original = findOriginalArray(changed)
print(original)
