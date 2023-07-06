# Implement a function to reverse the order of words in a given sentence.

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

# Example usage
input_sentence = "Hello, world! Welcome to the programming world."
reversed_sentence = reverse_sentence(input_sentence)
print(reversed_sentence)
