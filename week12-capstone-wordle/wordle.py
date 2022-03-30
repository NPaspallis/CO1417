def print_frequencies(words: [str]):
    """
    Prints the frequencies for each letter 'a' to 'z', as found in the given list of words.
    :param words: a list of string containing the words to count the letters for
    """
    # todo


def find_words_with_letters(words: [str], letters: [str]) -> [str]:
    """
    Find all words in the given list, which match all the given letters.
    For example for letters ['a', 'd', 'n'] and words list ['and', 'din', 'aid', 'dan'], return ['and', 'dan'].
    :param words: the list of words to be checked
    :param letters: the list of letters to be matched
    :return: a sublist of words which match the given characters
    """
    # todo


def check(secret: str, check_word: str) -> [str]:
    """
    Given a secret word and a check_word, which must be of equal length, return a list of words which
    are either 'gray', 'yellow' or 'green'. The semantics match the rules of Wordle:
    - 'gray' if the checked character does not appear in the secret word
    - 'yellow' if the checked character does appear in the secret word, but not in the same position
    - 'green' if the checked character matches the character at the same position in the secret word.
    For example for the secret word 'store' and check_word 'raise', it should return the list
    ['yellow', 'gray', 'gray', 'yellow', 'green']
    :param secret: a word to be checked against
    :param check_word: another word of equal length to be checked based on Wordle's rules
    :return: a list containing the values 'gray', 'yellow', 'green'
    """
    # todo


def find_word(words: [str], grays: [str], yellows: {}, greens: {}):
    """
    Given a list of words and constraints, it returns a suitable word, if it exists, otherwise the constant 'None'.
    The constraints are:
    - grays: A list of characters which are known to not exist in the target word
    - yellows: A dictionary of characters to sets of indices. The keys are characters, and the corresponding values
        are sets of integers, indicating the indices where it is known that the corresponding character is NOT at.
    - greens: A dictionary of characters to sets of indices. The keys are characters, and the corresponding values
        are sets of integers, indicating the indices where it is known that the corresponding character is found at.
    For example, the call:
        find_word(['batch', 'ozone'], 'abcd', {'n': {2}, 'z': {2, 3}}, {'o': {0, 2}, 'e': {4}})
    It looks for a word in the given list so that it does not contain any of the characters 'a', 'b', 'c', 'd'.
    Also it contains 'n' but not at index 2, and 'z' but not at indices 2, or 3.
    Finally, it contains 'o' at indices 0, 2, and it also contains 'e' at index 4.
    This for example excludes 'batch' but could return 'ozone'.
    remember that the indices are 0-base which means the first position is index 0, and the last one (5th) is index 4.
    :param words: the list of words to be checked against the constraints
    :param grays: a list of characters in the form of a string (gray constraint)
    :param yellows: a dictionary of characters to set of indices (yellow constraint)
    :param greens: a dictionary of characters to set of indices (green constraint)
    :return: a word from the given list which satisfies the constraints, or None if none is found
    """
    # todo
