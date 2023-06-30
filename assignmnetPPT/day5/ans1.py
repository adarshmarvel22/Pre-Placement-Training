def construct2DArray(original, m, n):
    if m * n != len(original):
        return []  # Return an empty 2D array if it is impossible
        
    return [original[i*n : (i+1)*n] for i in range(m)]

# Driver code to test the function
original = [1, 2, 3, 4]
m = 2
n = 2

result = construct2DArray(original, m, n)
print(result)
