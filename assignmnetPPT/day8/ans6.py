from collections import Counter

def findAnagrams(s, p):
    result = []
    freqP = Counter(p)
    freqWindow = Counter()

    start, end = 0, 0
    windowSize = len(p)
    sSize = len(s)

    while end < sSize:
        freqWindow[s[end]] += 1

        if end - start + 1 == windowSize:
            if freqWindow == freqP:
                result.append(start)
            freqWindow[s[start]] -= 1
            if freqWindow[s[start]] == 0:
                del freqWindow[s[start]]
            start += 1

        end += 1

    return result
s = "cbaebabacd"
p = "abc"
result = findAnagrams(s, p)
print(result)  # Output: [0, 6]
