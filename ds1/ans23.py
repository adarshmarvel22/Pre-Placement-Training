# Write a program to find the prime factors of a given number.

def find_prime_factors(number):
    prime_factors = []
    divisor = 2
    
    while divisor <= number:
        if number % divisor == 0:
            prime_factors.append(divisor)
            number //= divisor
        else:
            divisor += 1
    
    return prime_factors

# Example usage
input_number = 56
factors = find_prime_factors(input_number)
print(f"The prime factors of {input_number} are: {factors}")
