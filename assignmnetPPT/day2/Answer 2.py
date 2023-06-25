from collections import Counter

def maxTypesOfCandies(candyType):
    n = len(candyType)
    max_candies = n // 2

    # Count the frequency of each candy type
    count = Counter(candyType)

    # Return the maximum number of different types of candies Alice can eat
    return min(max_candies, len(count.keys()))

# Driver code
candyType = [1, 1, 2, 2, 3, 3]
result = maxTypesOfCandies(candyType)
print("Maximum number of different types of candies Alice can eat:", result)
