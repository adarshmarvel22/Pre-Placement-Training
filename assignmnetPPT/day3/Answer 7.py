def findMissingRanges(nums, lower, upper):
    ranges = []
    prev = lower - 1

    for num in nums:
        if num > prev + 1:
            ranges.append(getRange(prev + 1, num - 1))
        prev = num

    if upper > prev:
        ranges.append(getRange(prev + 1, upper))

    return ranges

def getRange(start, end):
    if start == end:
        return [start]
    else:
        return [start, end]

# Driver code
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
result = findMissingRanges(nums, lower, upper)
print("Missing ranges:", result)
