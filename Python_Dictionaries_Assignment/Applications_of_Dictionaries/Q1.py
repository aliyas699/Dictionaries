# Input string
input_string = "hello world hello python world"

# Split the string into words
words = input_string.split()

# Initialize an empty dictionary to store word counts
word_count = {}

# Iterate through the words and count occurrences
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word count dictionary
print(word_count)
