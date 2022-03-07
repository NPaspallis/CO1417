# This program defines a function to produce all combinations of n-sized words

def word_generator(num_of_letters):
    """
    Returns an iterator which produces a sequence of all possible combinations of n-sized words.
    For example, for num_of_letters=5, it produces: 'aaaaa', 'aaaab', 'aaaac', ..., 'zzzzx', 'zzzzy', 'zzzzz'.
    """
    first_word = 'a' * num_of_letters  # c is initialized as num_of_letters copies of 'a', e.g. 'aaaaa' for 5
    c = list(first_word)  # converts string to a list of characters
    while True:
        word = "".join(c)  # joins characters in list to produce string
        yield word
        exhausted = True
        # move on to next word
        for j in range(num_of_letters-1, -1, -1):  # get numbers from num_of_letters-1 down to 0
            if c[j] < 'z':
                c[j] = chr(ord(c[j]) + 1)  # modify j-th character, move to next character in alphabet
                exhausted = False
                break
            else:
                c[j] = 'a'

        # if we reach this point with the 'exhausted' flag still up, it means there is nothing more to do
        if exhausted:
            return


if __name__ == "__main__":  # this means: execute the following code only when run as a file (not when imported as a library)
    word_size = 5
    print("Generating words for word length: N = %d ..." % word_size)
    words = list(word_generator(word_size))  # the 'list()' is forcing the iterator to execute and produce the result
    num_of_words = len(words)
    print(words[0])
    print(words[1])
    print("...")
    print(words[num_of_words-2])
    print(words[num_of_words-1])
    print("Number of words: ", num_of_words)
