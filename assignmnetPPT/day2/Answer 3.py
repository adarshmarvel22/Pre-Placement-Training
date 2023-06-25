def findLHS(nums):
    count = {}
    longest_subsequence = 0

    # Count the frequency of each number
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # Check each number and its adjacent number
    for num in count:
        if num + 1 in count:
            longest_subsequence = max(longest_subsequence, count[num] + count[num + 1])

    return longest_subsequence

# Driver code
nums = [1, 3, 2, 2, 5, 2, 3, 7]
result = findLHS(nums)
print("Length of the longest harmonious subsequence:", result)
