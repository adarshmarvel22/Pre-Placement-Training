def findDisappearedNumbers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    
    answer1 = list(set1 - set2)
    answer2 = list(set2 - set1)
    
    return [answer1, answer2]

nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = findDisappearedNumbers(nums1, nums2)
print(result)
