# Capstone project: Wordle

Wordle is a word-based game. The game name is a play on the  surname of its creator,
[Josh Wardle](https://en.wikipedia.org/wiki/Josh_Wardle).
The game experienced viral growth in late 2021:

> ...the number of players exploded from 90 on November 1 to 300,000 on January 2 and 
> more than 2 million a week later (source: [statista.com](https://www.statista.com/chart/26667/usage-of-wordle-and-other-online-games-in-the-us/)).

The game was bought by the [New York Times](https://www.nytimes.com/2022/01/31/business/media/new-york-times-wordle.html) for an undisclosed amount
(estimated to be 2-3 million dollars) in January, 2022.

## Rules

Players have six attempts to guess a five-letter word, with feedback given for each guess 
in the form of colored tiles indicating when letters match or occupy the correct position.

<img src=wordle.png alt='Wordle - solution of puzzle #275 (released on the 21st of March 2022)' width=320>

_The screenshot above shows the solution of puzzle #275 (released on the 21st of March 2022)_

After every guess, each letter is marked as either green, yellow or gray:
- **green** indicates that letter is correct and in the correct position,
- **yellow** means it is in the answer but not in the right position, 
- **gray** indicates it is not in the answer at all.

### Words

As you may recall, in [week 09](../week09-password-cracking), we provided a file containing almost sixteen
thousand 5-letter words: [words_5_letters.txt](../week09-password-cracking/step0905/words_5_letters.txt).

However, the words available in the puzzle is actually a subset of the full list of 5-letter English words,
approximately thirteen thousands. The list of used words can be accessed via the 
[source code](https://www.nytimes.com/games/wordle/main.b84b7aa7.js) of the game (you will notice the code is
not very readable, as the JavaScript was minified/compressed). Nevertheless, we have copied those words in the file
[wordles.txt](wordles.txt).

## Requirements:

For this capstone, you are required to realize algorithms and data structures which
help solve the Wordle puzzle.

There are individual requirements, each one of which corresponds to a function.
To achieve each marking level, you need to implement one of the corresponding functions, which
are in incremental order of difficulty.

Briefly for this capstone project you are required to:
1. Build a function which computes the frequency of each letter as it appears in a given list of words.
2. Build a function which for a given list of words and a given list of letters it returns only those words which contain the given letters.
3. Build a function which realizes the Wordle check: for a given secret word and an attempted solution, ιτ returns a list of colors as per Wordle's rules.
4. Build a function which, given a list of words and some constraints, it finds a possible answer to the Wordle puzzle.

See the Marking scheme below for details on what to build for each function.
Additionally, see the template file [wordle.py](wordle.py) with the signature and documentation
for each required function.

## Marking scheme:

### Pass (40%)
* Implement a function named ``print_frequencies(words: [str])`` which given a list of words, it prints a list of all letters found in
these words, and their frequency (i.e., the number of times each letter is encountered).
* The function must print the letters sorted by frequency in
descending order, i.e., the letter with the highest frequency shows on top.

* See sample runs below for more info.

The call ``print_frequencies(['hello', 'world'])`` produces the output:
```text
l 3
o 2
h 1
e 1
w 1
r 1
d 1
```

The call ``print_frequencies(wordles)`` (where ``wordles`` is the list of all words in file [wordles.txt](wordles.txt)) produces the output:
```text
s 6665
e 6662
a 5990
o 4438
r 4158
i 3759
l 3371
t 3295
n 2952
u 2511
d 2453
y 2074
c 2028
p 2019
m 1976
h 1760
g 1644
b 1627
k 1505
f 1115
w 1039
v 694
z 434
j 291
x 288
q 112
```

### Lower Second (50%)
* Implement function ``find_words_with_letters`` which given a list of words, and a list of letters, it returns the list
of all words which contain exactly the given letters.
* For example see the following sample runs.

The call ``find_words_with_letters(['and', 'din', 'aid', 'dan'], ['a', 'd', 'n'])`` returns the list:
```text
['and', 'dan']
```

Given the frequencies found before for the Wordle's words, we can find an optimal starting word by selecting some
which contains the most frequent letters: s, e, a, o, r.
In this case, the call ``find_words_with_letters(wordles, ['s', 'e', 'a', 'o', 'r'])`` returns the list:
```text
['arose', 'aeros', 'soare']
```

### Upper Second (60%)
* Build a function ``check(secret, check_word)`` which given a secret word, and a test word, it realizes Wordle's rules to return a
list of colors accordingly. The colors are either 'gray', 'yellow' or 'green' with the standard Wordle's semantics:
    - 'gray' if the checked character does not appear in the secret word
    - 'yellow' if the checked character does appear in the secret word, but not in the correct position
    - 'green' if the checked character matches the character at the same position in the secret word.
* For example see the following sample runs.

The call ``check('level', 'sofas')`` with no matches, returns the list:
```text
['gray', 'gray', 'gray', 'gray', 'gray']
```

The call ``check('store', 'crazy')`` with just one match at a different position, returns the list:
```text
['gray', 'yellow', 'gray', 'gray', 'gray']
```

The call ``check('crane', 'raise')`` with some partial and one fully correct match, returns the list:
```text
['yellow', 'yellow', 'gray', 'gray', 'green']
```

### First (70%)
* Build a function titled ``find_word`` which given a list of words and constraints, it returns a suitable word
(if it exists), otherwise it returns the constant ``None``.
The constraints are:
  - grays: A list of characters which DO NOT exist in the target word
  - yellows: A dictionary of characters to sets of indices. The keys are characters, which exist in the target word, but NOT in the indices specified by the corresponding values (provided as sets of integers).
  - greens: A dictionary of characters to sets of indices. The keys are characters, and the corresponding values are sets of integers, indicating the indices where the corresponding character is found at.
* This function returns a word from the given list which satisfies the given constraints, or ``None`` if no such word is found
* For example, consider the call:

``find_word(['batch', 'ozone'], ['a', 'b', 'c', 'd'], {'n': {2}, 'z': {2, 3}}, {'o': {0, 2}, 'e': {4}})``

* In this example, the search takes place in the given list of words: ``batch`` and ``ozone``.
* The word ``ozone`` satisfies the constraints:
  - grays: It does NOT contain any of the characters 'a', 'b', 'c', 'd'.
  - yellows: It contains 'n' but not at index 2, and 'z' but not at indices 2, or 3.
  - Finally, greens: It contains 'o' at indices 0, 2, and it also contains 'e' at index 4.

* Therefore, this example would return ``ozone`` but would exclude ``batch``.

> Remember that the indices are 0-base which means the first position is index 0, and the last one (5<sup>th</sup>) is index 4.

* For example see the following sample runs.

The call ``find_word(wordles, ['i', 'o', 'u', 'l', 'd', 'w', 't'], {'s': {1, 2}, 'p': {3}}, {'s': {0}, 'a': {2}})``
returns the word:
```text
space
```

The call ``find_word(wordles, ['m'], {'p': {2, 3}, 'd': {0}}, {'a': {1, 4}})`` returns the word:
```text
panda
```

And the call ``find_word(wordles, 'aeiouyrwt', {}, {})`` returns no word:
```text
None
```

### High First (80%+)
* Build a console-based Wordle game.
* You can reuse code developed in the previous steps, such as the ``check`` function.
* Provide two modes of play: auto and interactive
* Keep a count of the number of valid tries.
* Print appropriate greetings at the beginning and finish of the game.
* No need to use graphics. You can implement the game as a text-based game where the input is provided via the keyboard
and the output is printed as text.
* In the interactive play mode, you should also check that the input is valid, and ignore invalid input.


* For example see the following sample runs.

  * Sample run with secret word ``coped``:
```text
Welcome to the text-based Wordle game.
I have guessed a secret word. Can you find it?
(Type "1" for auto game, "2" for interactive game, or "quit" to exit)
Enter your choice: 1

Trying: penes
->  ['yellow', 'yellow', 'gray', 'green', 'gray']

Trying: lapel
->  ['gray', 'gray', 'green', 'green', 'gray']

Trying: hyper
->  ['gray', 'gray', 'green', 'green', 'gray']

Trying: biped
->  ['gray', 'gray', 'green', 'green', 'green']

Trying: coped
->  ['green', 'green', 'green', 'green', 'green']
Congratulations! You found the wordle in 5 tries
Bye!
```

* Sample run with secret word ``anode``:
```text
Welcome to the text-based Wordle game.
I have guessed a secret word. Can you find it?
(Type "1" for auto game, "2" for interactive game, or "quit" to exit)
Enter your choice: 2

Enter a 5 letter word: raise
1 -> ['gray', 'yellow', 'gray', 'gray', 'green']

Enter a 5 letter word: craze
2 -> ['gray', 'gray', 'yellow', 'gray', 'green']

Enter a 5 letter word: above
3 -> ['green', 'gray', 'green', 'gray', 'green']

Enter a 5 letter word: alone
4 -> ['green', 'gray', 'green', 'yellow', 'green']

Enter a 5 letter word: anode
5 -> ['green', 'green', 'green', 'green', 'green']
Congratulations! You found the wordle in 5 tries
Bye!
```

* Sample run with invalid input and quit:
```text
Welcome to the text-based Wordle game.
I have guessed a secret word. Can you find it?
(Type "1" for auto game, "2" for interactive game, or "quit" to exit)
Enter your choice: something
Enter your choice: 2

Enter a 5 letter word: abc
abc is not 5 letters long

Enter a 5 letter word: abcde
abcde is not in the list of accepted words

Enter a 5 letter word: hello
1 -> ['gray', 'yellow', 'gray', 'gray', 'yellow']

Enter a 5 letter word: quit
Bye!
```

### Hints
- If you are not very familiar with Wordle, it might be a good idea to try it a few times first before attempting
to solve this capstone project. You can play it online at [NYTimes](https://www.nytimes.com/games/wordle/index.html).
- You can use the function signatures shown in file [wordles.py](wordle.py) as a starting point.
These signatures are also listed below.

```python
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
    For example, consider the call:
        find_word(['batch', 'ozone'], 'abcd', {'n': {2}, 'z': {2, 3}}, {'o': {0, 2}, 'e': {4}})
    It looks for a word in the given list so that it does not contain any of the characters 'a', 'b', 'c', 'd'.
    Also it contains 'n' but not at index 2, and 'z' but not at indices 2, or 3.
    Finally, it contains 'o' at indices 0, 2, and it also contains 'e' at index 4.
    This for example excludes 'batch' but could return 'ozone'.
    Remember that the indices are 0-base which means the first position is index 0, and the last one (5th) is index 4.
    :param words: the list of words to be checked against the constraints
    :param grays: a list of characters in the form of a string (gray constraint)
    :param yellows: a dictionary of characters to set of indices (yellow constraint)
    :param greens: a dictionary of characters to set of indices (green constraint)
    :return: a word from the given list which satisfies the constraints, or None if none is found
    """
    # todo
```
