# Implement a function to calculate the product of all elements in a list.

def calculate_product(numbers):
    # Initialize the product variable to 1
    product = 1

    # Multiply each number in the list to the product
    for num in numbers:
        product *= num

    # Return the product
    return product

# Test the function
number_list = [2, 3, 4, 5]
result = calculate_product(number_list)
print("Product of all elements:", result)
