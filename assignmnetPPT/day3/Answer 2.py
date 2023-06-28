def fourSum(nums, target):
    nums.sort()  # Sort the input array
    quadruplets = []
    n = len(nums)

    for a in range(n - 3):
        # Skip duplicate values for 'a'
        if a > 0 and nums[a] == nums[a - 1]:
            continue

        for b in range(a + 1, n - 2):
            # Skip duplicate values for 'b'
            if b > a + 1 and nums[b] == nums[b - 1]:
                continue

            left = b + 1  # Pointer for the element to the right of nums[b]
            right = n - 1  # Pointer for the last element in the array

            while left < right:
                current_sum = nums[a] + nums[b] + nums[left] + nums[right]

                if current_sum == target:
                    quadruplets.append([nums[a], nums[b], nums[left], nums[right]])

                    # Skip duplicate values for 'left' and 'right'
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return quadruplets


# Driver code
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = fourSum(nums, target)
print(result)
