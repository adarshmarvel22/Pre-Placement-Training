from collections import Counter

def findOriginalArray(changed):
    counter = Counter(changed)
    res = []
    for k in counter.keys():
        
        if k == 0:
            # handle zero as special case
            if counter[k] % 2 > 0:
                return []
            res += [0] * (counter[k] // 2)
            
        elif counter[k] > 0:
            x = k
            
            # walk down the chain
            while x % 2 == 0 and x // 2 in counter:
                x = x // 2
                
            # walk up and process all numbers within the chain. mark the counts as 0
            while x in counter:
                if counter[x] > 0:
                    res += [x] * counter[x]
                    if counter[x+x] < counter[x]:
                        return []
                    counter[x+x] -= counter[x]
                    counter[x] = 0
                x += x
    return res

changed = [1, 3, 4, 2, 6, 8]
original = findOriginalArray(changed)
print(original)
