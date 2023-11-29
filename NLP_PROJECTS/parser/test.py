"""import nltk

# Create a basic sentence structure
sentence = nltk.Tree('S', [nltk.Tree('NP', ['John']), nltk.Tree('VP', ['runs'])])

# Set a label for the NP subtree
sentence[0].set_label('Subject')

# Retrieve the label of the VP subtree
vp_label = sentence[1][0]

print("Label of NP:", sentence[0].label())
print("Label of VP:", vp_label)
print(sentence)

import nltk

# Create a basic sentence structure
sentence = nltk.Tree('S', [nltk.Tree('NP', ['John']), nltk.Tree('VP', ['runs'])])

# Access and set a label for the NP subtree
for subtree in sentence:
    print(subtree)

# Retrieve the label of the VP subtree
vp_label = sentence[1].label()

print("Label of NP:", sentence[0].label())
print("Label of VP:", vp_label)
"""
from transformers import AutoTokenizer

# Load a pre-trained tokenizer (e.g., 'bert-base-uncased')
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

# Input text
text = "The quick brown fox jumps over the lazy dog."

# Tokenize the input text
tokens = tokenizer.tokenize(text)

# Print the tokens
print(tokens)