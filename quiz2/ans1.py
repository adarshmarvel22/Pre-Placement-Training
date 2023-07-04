def get_even_numbers(input_list):
    return [num for num in input_list if num % 2 == 0]

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(input_list)
print(even_numbers)  # Output: [2, 4, 6, 8, 10]