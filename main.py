# Text File Analyzer
'''There is a sample.txt file attached to this project. 
The project reads sample.txt, you can paste your text there or can use a new file of yours.'''

with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Counting characters (excluding spaces and newlines)
characters = len(content.replace(" ", "").replace("\n", "").lower())
print("The number of characters in the given file are:", characters)

# Counting words
words = content.split()
no_of_words = len(words)
print("The number of words in the given file are:", no_of_words)

# Counting sentences (basic check for trailing period)
no_of_sentences = len(content.split(".")) 
if content.strip().endswith("."):
    no_of_sentences -= 1
print("The number of sentences in the given file are:", no_of_sentences)

# Finding the most common word
frequency_dict = {}
for word in words:
    if word in frequency_dict:
        frequency_dict[word] += 1
    else:
        frequency_dict[word] = 1

highest_value = 0
highest_key = ""

for key in frequency_dict:
    if frequency_dict[key] > highest_value:
        highest_value = frequency_dict[key]
        highest_key = key

print("The most common word in the file is:", highest_key)

# Calculating average sentence length (by characters without spaces)
sentences = content.lower().replace(" ", "").split(".")
lengths = [len(sentence) for sentence in sentences if sentence.strip()]
avg_sentence_length = sum(lengths) / len(lengths)

print("The average sentence length in the given file is:", avg_sentence_length)

               
        
        


    
 