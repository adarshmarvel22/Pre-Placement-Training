# Implement a function to calculate the Fibonacci sequence up to a given number of terms.

def fibonacci_sequence(n):
    sequence = []
    if n >= 1:
        sequence.append(0)
    if n >= 2:
        sequence.append(1)
    if n > 2:
        for i in range(2, n):
            next_number = sequence[i - 1] + sequence[i - 2]
            sequence.append(next_number)
    return sequence

# Example usage
num_terms = 10
fib_sequence = fibonacci_sequence(num_terms)
print(fib_sequence)
