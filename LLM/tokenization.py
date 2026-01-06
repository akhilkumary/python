# Regular Expression
import re

with open('the-verdict.txt', 'r', encoding = 'utf-8') as f:
    raw_text = f.read()

print(f"Total number of characters, {len(raw_text)}")
print(raw_text[:99])

# Step 1: Tokenize the text: Split the text into tokens

# splitting when a space is encountered
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)

# Filtering out empty strings by striping whitespaces - ''.strip() returns False
preprocessed = [item for item in preprocessed if item.strip()]

print(f"Initial size of the list of tokens is {len(preprocessed)}.")

# Step 2: Build a volcabulary - List of tokens in alphabetical order
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)

print(f"Vocabulary Size is {vocab_size}.")

vocab = {token:integer for integer, token in enumerate(all_words)}

# printing the vocabulary
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break

    