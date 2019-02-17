# Write a function called "word_count", which takes a filename and a list
# of words as arguments. It then opens the file, reads it line by line and
# checks if the specified words occur in that line. If so, the counter for
# the appearing word is increased. At the end, it returns a dictionary,
# which contains in how many lines each word occurred.
def word_count(filename, wordlist):
    with open(filename, 'r') as file:
        lines = file.readlines()
        word_dictionary = { key: 0 for key in wordlist }
        for line in lines:
            for word in wordlist:
                if word in line:
                    word_dictionary[word] += 1

    return word_dictionary



