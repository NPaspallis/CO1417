# Password Cracking

When you sign up to a new service (like Google, Facebook, etc.) you are generally asked to provide a password.
The providers do not generally keep the plaintext version of your password, because if they are compromised
(i.e., the passwords are *leaked*) then it would be very easy for anyone who got access to them, to exploit them.

Instead, the providers store a *hashed* version of the password.

      The hashed form of a password is also called a cipher

Even when leaked, a hashed password cannot be
(immediately) used - you need to work your way back to the plaintext version first. Since the *cipher* is produced
using one-way functions though, that is not simple.

This step aims to study how *password cracking* works, and to highlight the importance for large, strong passwords.

In this and the following steps we examine:
 - How brute force password attacks work
 - How dictionary password attacks work
 - How demanding is the brute force approach compared to dictionary based password attack

## Assumptions

- All passwords, when in plaintext, consist of lower-case letters only, i.e. 'a' to 'z' - no capitals, no digits, no
  gaps, and no punctuation.
- To keep it manageable, assume all passwords are 5-letters long.

## Exercises

- Compute mathematically, how many valid combinations there are for 5-letter passwords, where the valid 
characters are the lower-case latin alphabet characters only.

- Examine the code in [word_generator.py](word_generator.py) which generates all the N-letter words from letters ``a`` to ``z``. For example for ``N = 3``:
```text
Generating words for word length: N = 3 ...
aaa
aab
...
zzy
zzz
Number of words:  17576
```

- Edit the code and run it also for ``N = 1`` and ``N = 5``. Do the resulting numbers match your expectations and calculations?
