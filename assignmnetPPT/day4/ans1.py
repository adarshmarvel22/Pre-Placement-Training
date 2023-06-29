def find_common_elements(arr1, arr2, arr3):
    p1, p2, p3 = 0, 0, 0
    result = []

    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
        if arr1[p1] == arr2[p2] == arr3[p3]:
            result.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        else:
            min_val = min(arr1[p1], arr2[p2], arr3[p3])
            if arr1[p1] == min_val:
                p1 += 1
            if arr2[p2] == min_val:
                p2 += 1
            if arr3[p3] == min_val:
                p3 += 1

    return result

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]

result = find_common_elements(arr1, arr2, arr3)
print(result)
