def array_pair_sum(nums):
    nums.sort()  # Sort the array in ascending order
    pair_sum = 0

    for i in range(0, len(nums), 2):
        pair_sum += nums[i]

    return pair_sum


# Driver code
nums = [1, 4, 3, 2]
result = array_pair_sum(nums)
print(result)
