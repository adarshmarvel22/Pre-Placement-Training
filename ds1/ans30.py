# Implement a function to find the minimum element in a rotated sorted list.

def find_minimum(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # If the middle element is greater than the rightmost element,
        # the minimum element is on the right side
        if nums[mid] > nums[right]:
            left = mid + 1
        # If the middle element is smaller than the rightmost element,
        # the minimum element is on the left side or is the middle element itself
        else:
            right = mid

    # When the loop ends, left and right will point to the minimum element
    return nums[left]

# Test the function
nums = [4, 5, 6, 7, 0, 1, 2]
minimum = find_minimum(nums)
print("Minimum element:", minimum)
