def maximumProduct(nums):
    nums.sort()  # Sort the array in ascending order

    # The maximum product can be achieved by multiplying the last three elements
    # (the largest elements) or the first two elements (if there are negative numbers)
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

# Driver code
nums = [1, 2, 3]
result = maximumProduct(nums)
print("Maximum product:", result)
