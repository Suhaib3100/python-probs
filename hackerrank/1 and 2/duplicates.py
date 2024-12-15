# Read the input line containing space-separated words
words = input("Enter the words: ")

# Split the words into a list
word_list = words.split()

# Initialize a dictionary to count occurrences of each word
word_count = {}

# Count each word in the list
for word in word_list:
    if word in word_count:
        word_count[word] += 1  # Increment count if the word is already in the dictionary
    else:
        word_count[word] = 1  # Initialize count to 1 for new words
        
# Prepare a list to hold duplicates
duplicates = {}

# Find duplicates with their counts
for word, count in word_count.items():
    if count > 1:  # Check for duplicates
        duplicates[word] = count  # Store word and its count

# Print the duplicate words and their counts
for word, count in duplicates.items():
    print(f"{word}: {count}")