def findMissingRanges(nums, lower, upper):
    ranges = []
    start = lower

    for num in nums:
        if num > start:
            # If there is a missing number between start and num - 1, create a range
            ranges.append(getRange(start, num - 1))
        start = num + 1

    # Check for missing numbers after the last element of nums
    if start <= upper:
        ranges.append(getRange(start, upper))

    return ranges


def getRange(start, end):
    # Helper function to format the range in the required format
    if start == end:
        return str(start)
    else:
        return str(start) + "->" + str(end)


# Driver code
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
result = findMissingRanges(nums, lower, upper)
print(result)
