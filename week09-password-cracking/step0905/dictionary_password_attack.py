# This initial code simply reads all the words from the file and inserts them in a list. Then it prints the list.
dictionary_words = []

print("Reading dictionary words from file ...")
file = open('words_5_letters.txt', 'r')  # open for read-only
all_lines = file.readlines()
for line in all_lines:
    dictionary_words.append(line.strip())  # strip clears non-visible characters, like 'next line'

for word in dictionary_words:
    print(word)

# TODO Implement the dictionary password attack and measure the time it takes to 'break' some words - see lists.py for more info
