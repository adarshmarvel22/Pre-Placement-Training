def validMountainArray(arr):
    n = len(arr)
    
    if n < 3:
        return False
    
    peak_index = arr.index(max(arr))
    
    if peak_index == 0 or peak_index == n - 1:
        return False
    
    for i in range(peak_index):
        if arr[i] >= arr[i + 1]:
            return False
    
    for i in range(peak_index, n - 1):
        if arr[i] <= arr[i + 1]:
            return False
    
    return True

# Driver code
arr = [2, 1]
print(validMountainArray(arr))
