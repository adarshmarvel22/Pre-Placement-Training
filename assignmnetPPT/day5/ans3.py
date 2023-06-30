def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    idx = n - 1
    
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[idx] = nums[left] * nums[left]
            left += 1
        else:
            result[idx] = nums[right] * nums[right]
            right -= 1
        idx -= 1
    
    return result

nums = [-4, -1, 0, 3, 10]
squared_nums = sortedSquares(nums)
print(squared_nums)
