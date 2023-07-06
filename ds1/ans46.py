# Implement a function to find the first missing positive

def find_first_missing_positive(nums):
    # Move all non-positive numbers to the beginning of the list
    next_positive = 0
    for i in range(len(nums)):
        if nums[i] <= 0:
            nums[i], nums[next_positive] = nums[next_positive], nums[i]
            next_positive += 1

    # Consider only the positive numbers after the non-positive numbers
    nums = nums[next_positive:]

    # Mark the presence of a positive number by negating the corresponding index
    for i in range(len(nums)):
        num = abs(nums[i])
        if num <= len(nums):
            nums[num - 1] = -abs(nums[num - 1])

    # Find the index of the first positive number
    for i in range(len(nums)):
        if nums[i] > 0:
            return i + 1

    # If all positive numbers from 1 to len(nums) are present, return len(nums) + 1
    return len(nums) + 1

# Test the function
number_list = [3, 4, -1, 1]
first_missing = find_first_missing_positive(number_list)
print("First missing positive integer:", first_missing)
