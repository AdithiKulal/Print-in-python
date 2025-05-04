class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()  # Split the string into words
        reversed_words = words[::-1]  # Reverse the word order
        return " ".join(reversed_words)  # Join the words back into a string

# Taking user input
sentence = input("Enter a sentence: ")

# Creating an instance of StringReverser with user input
reverser = StringReverser(sentence)

# Printing the reversed sentence
print("Reversed sentence:", reverser.reverse_words())