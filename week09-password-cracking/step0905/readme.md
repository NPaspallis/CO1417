# Password Cracking

When you sign up to a new service (like Google, Facebook, etc.) you are generally asked to provide a password.
The providers do not generally keep the plaintext version of your password, because if they are compromised
(i.e., the passwords are *leaked*) then it would be very easy for anyone who got access to them, to exploit them.

Instead, the providers store a *hashed* version of the password.

      The hashed form of a password is also called a cipher

Even when leaked, a hashed password (*cipher*) cannot be (immediately) used - you need to work your way back to the
plaintext version first. Since the *cipher* is produced using one-way functions though, that is not simple.

This step aims to study how *password cracking* works, and to highlight the importance for large, strong passwords.

In this step we examine:
 - How brute force password attacks work
 - How dictionary password attacks work
 - How demanding is the brute force approach compared to dictionary based password attack

### Assumptions

- All passwords when in plaintext consist of lower-case letters only, i.e. 'a' to 'z' - no capitals, no digits, no
  gaps, and no punctuation.
- To keep it manageable, assume all passwords are 5-letter long.
- You are provided with the file [words_5_letters.txt](words_5_letters.txt) which contains 15918 words. These are
all the valid English words consisting of 5 letters exactly, such as ``world``.

## Brute force password attack

You are given a *cipher* which you know was produced using MD5. Your only knowledge is that the corresponding password
consists of **lower case latin characters** only, and that it is **5 characters long**.

The **Brute force password attack** works as follows:
- Generate all possible passwords
- For each password, compute their MD5 and check if it matches your *cipher*
- If yes, then you found the password, so you can terminate the loop, else keep looking

### Exercise
- Add code in the [brute_force_password_attack.py](brute_force_password_attack.py) file to realize the 
*Brute force password attack* described above. You can (and probably should) use code from previous steps.
- Add code in the same file to *measure* the time it takes to complete this attack.
- You can verify your code using the following password/cipher combinations:
  - ``world -> 7d793037a0760186574b0282f2f435e7``
  - ``bezel -> 5d41402abc4b2a76b9719d911017c592``
  - ``early -> 2b3de800b4576343a07e86b8c420e448``
  - ``abcde -> ab56b4d92b40713acc5af89985d4b786``

## Dictionary password attack

We have seen before that there are 11,881,376 combinations of 5-letter words. Of course, many are meaningless
combinations like ``abcde`` and ``xyzxy``.
If we could *assume* that the password is a valid English word, then the domain of possible words would be
significantly smaller.

In this folder we have included the [words_5_letters.txt](words_5_letters.txt) file, which contains the valid
English words consisting of 5 letters. If you double-click it and open it, you can see that its size is 15,918 words.
This is 746 times fewer possibilities, when compared to all possible combinations.

### Exercise

- Add code in the [dictionary_password_attack.py](dictionary_password_attack.py) file to realize the dictionary attack. 
  - First, write code to print all the words in the [words_5_letters.txt](words_5_letters.txt) file.
  - Next write code which implements the *dictionary password attack*.
- Add code in the same file to *measure* the time it takes to complete this attack.
- Like before, you can verify your code using the following password/cipher combinations:
  - ``world -> 7d793037a0760186574b0282f2f435e7``
  - ``bezel -> 5d41402abc4b2a76b9719d911017c592``
  - ``early -> 2b3de800b4576343a07e86b8c420e448``
  - ``abcde -> ab56b4d92b40713acc5af89985d4b786`` for this, your code should simply say that no password found as ``abcde`` is not in the dictionary

- Compare the measured time needed for the *Brute force password attack* with the time needed for the *Dictionary password attack*.
