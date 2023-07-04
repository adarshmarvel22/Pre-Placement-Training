def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean


# driver code and given example

data = [10, 15, 20, 25, 30]
mean_value = calculate_mean(data)
print("Mean:", mean_value)