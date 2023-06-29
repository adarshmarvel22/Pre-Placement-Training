def sorted_squares(nums):
    squared_nums = [num**2 for num in nums]  # Square each number in nums
    squared_nums.sort()  # Sort the squared numbers in non-decreasing order
    return squared_nums


# Driver code
nums = [-4, -1, 0, 3, 10]
result = sorted_squares(nums)
print(result)
