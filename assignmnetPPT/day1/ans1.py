def find_indices(nums, target):
    """
    Finds the indices of the two numbers in the array that add up to the target.

    Args:
        nums: The array of integers.
        target: The target sum.

    Returns:
        A list of the two indices, in any order.
    """

    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
         return [i, seen[diff]]
        else:
         seen[num] = i
    return []
 
# Driver Code
if __name__ == "__main__":
    nums = [2,7,11,15]
    nums_size = 4
    target=9
    ans = find_indices(nums, target)
    print(ans)