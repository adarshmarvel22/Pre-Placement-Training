def findTheDistanceValue(arr1, arr2, d):
    distance = 0
    for num1 in arr1:
        is_valid = True
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                is_valid = False
                break
        if is_valid:
            distance += 1
    return distance

arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
distance = findTheDistanceValue(arr1, arr2, d)
print(distance)
