def threeSumClosest(nums, target):
    nums.sort()  # Sort the input array
    closest_sum = float('inf')  # Initialize the closest sum to infinity

    for i in range(len(nums)-2):
        left = i + 1  # Pointer for the element to the right of nums[i]
        right = len(nums) - 1  # Pointer for the last element in the array

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]  # Calculate the current sum

            if current_sum == target:
                return current_sum  # Return the sum if it equals the target exactly

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum  # Update the closest sum if necessary

            if current_sum < target:
                left += 1  # Move the left pointer to the right
            else:
                right -= 1  # Move the right pointer to the left

    return closest_sum


# Driver code
nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
print(result)
