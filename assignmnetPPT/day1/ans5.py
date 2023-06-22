def merge_sorted_arrays(nums1, m, nums2, n):
  """
  Merges the two sorted arrays nums1 and nums2 into a single sorted array.

  Args:
    nums1: The first sorted array.
    m: The number of elements in nums1.
    nums2: The second sorted array.
    n: The number of elements in nums2.

  Returns:
    The merged sorted array.
  """

  i = 0
  j = 0
  k = 0
  while i < m and j < n:
    if nums1[i] <= nums2[j]:
      nums1[k] = nums1[i]
      i += 1
    else:
      nums1[k] = nums2[j]
      j += 1
    k += 1
  while i < m:
    nums1[k] = nums1[i]
    i += 1
    k += 1
  while j < n:
    nums1[k] = nums2[j]
    j += 1
    k += 1


def main():
  nums1 = [1, 2, 3, 0, 0, 0]
  m = 3
  nums2 = [2, 5, 6]
  n = 3
  merge_sorted_arrays(nums1, m, nums2, n)
  print(nums1)


if __name__ == "__main__":
  main()