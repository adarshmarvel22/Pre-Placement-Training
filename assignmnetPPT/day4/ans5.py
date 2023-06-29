import math

def arrange_coins(n):
    k = int(math.sqrt(2 * n))  # Calculate the maximum k (number of rows) using the formula
    while (k * (k + 1)) // 2 > n:  # Adjust k if the number of coins is not sufficient for k rows
        k -= 1
    return k


# Driver code
n = 5
result = arrange_coins(n)
print(result)
