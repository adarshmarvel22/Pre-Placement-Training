def findDuplicates(nums):
    duplicates = []
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] < 0:
            duplicates.append(abs(num))
        else:
            nums[idx] *= -1
    return duplicates

nums = [4, 3, 2, 7, 8, 2, 3, 1]
duplicates = findDuplicates(nums)
print(duplicates)
