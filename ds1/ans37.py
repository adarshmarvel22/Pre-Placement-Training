# Write a Python program to reverse the order of words in a sentence while preserving the word order.

def reverse_sentence(sentence):
    # Split the sentence into words using whitespace as the delimiter
    words = sentence.split()

    # Reverse the order of words
    reversed_words = words[::-1]

    # Join the reversed words into a new sentence
    reversed_sentence = ' '.join(reversed_words)

    # Return the reversed sentence
    return reversed_sentence

# Test the function
input_sentence = input("Enter a sentence: ")
reversed_result = reverse_sentence(input_sentence)
print("Reversed sentence:", reversed_result)
