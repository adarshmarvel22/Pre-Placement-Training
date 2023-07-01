def minProductSum(nums1, nums2):
    nums1.sort()
    nums2.sort(reverse=True)
    
    n = len(nums1)
    min_product_sum = sum(nums1[i] * nums2[i] for i in range(n))
    
    return min_product_sum

# Driver code
nums1 = [5, 3, 4, 2]
nums2 = [4, 2, 2, 5]
print(minProductSum(nums1, nums2))
