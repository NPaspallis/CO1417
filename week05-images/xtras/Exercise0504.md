# Exercise 0504 - Reading Hex-encoded images

In this exercise you are asked to edit the code of [bitmap.py](../step0505/bitmap.py) (or the corresponding edited
code of [bitmap_compact.py](../step0506/bitmap_compact.py)), so that it can read the file ``universum-hex.txt``,
encoded with the more compact Hexadecimal encoding described in [step0506](../step0506/readme.md).

Important: When you copy-paste the code, remember to edit the file name so you are reading the correct file:
``universum-hex.txt``.

Hint 1: You can use the ``ord()`` function of Python to get the *order* of a character in the
[ASCII table](https://www.rapidtables.com/code/text/ascii-table.html).
For example:

```python
ord('0')  # returns 48
ord('1')  # returns 49
...
ord('9')  # returns 57
ord('A')  # returns 65
ord('B')  # returns 66
...
ord('F')  # returns 70
```


Hint 2: You can check individual bits of a number using the ``&`` bitwise operator.
For example:

```python
a = 10  # last 8 bits are 00001010
b7 = a & 128 != 0  # False (because the 8th least significant bit is zero)
...
b3 = a & 8 != 0  # True  (because the 4th least significant bit is one)
b2 = a & 4 != 0  # False (because the 3rd least significant bit is zero)
b1 = a & 2 != 0  # True  (because the 2nd least significant bit is one)
b0 = a & 1 != 0  # False (because the 8th least significant bit is zero)
```

Note that the *least-significant-bit* is the one all the way to the right (because a change in its value has the least
impact), and the *most-significant-bit* is the one all the way to the left (as a change in its value has the greatest
impact).
