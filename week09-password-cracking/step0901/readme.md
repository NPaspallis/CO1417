# Hashing

Hashing is the process of converting a key into another value. This has many applications, including in data
structures, and in security.

- A **hash function** is used to generate the new value according to a mathematical algorithm.
- The result of a hash function is known as a hash value or simply, a **hash**.
- A good hash function uses a **one-way hashing algorithm**, or in other words, the hash cannot be converted back into the original key.
- It is possible for a hash function to produce the same hash for two or more different keys, which we refer to as **collisions**.
- A good hashing algorithm is fast and minimizes collisions.

## Examples

Consider the following simple hashing functions:

1. ``f(key) -> 1`` This function always produces the same hash value ``1`` for every key.
It is a valid hash function but a very bad one as everything results to a collision:
    - ``f('hello') -> 1``
    - ``f('world') -> 1``
    - ``f('20') -> 1``
    - ``f('player') -> 1``
    - ``f('replay') -> 1``

2. ``f(key) -> length(key)`` This hash function computes the hash as equal to the length of the key in characters.
It is better than the previous hash function but still has many collisions.
    - ``f('hello') -> 5``
    - ``f('world') -> 5``
    - ``f('20') -> 2``
    - ``f('player') -> 6``
    - ``f('replay') -> 6``
3. ``f(key) -> order(key[0]) + order(key[1]) + ...`` This hash function computes the hash as the sum of the order of the individual characters.
The order of a character is the index at which it appears in the ASCII table. Python provides the ``ord`` function which
can be used to easily compute the order. For example, ``ord('a') -> 97`` and ``ord('A') -> 65``. The corresponding
values can be verified by looking them up in the ASCII table: https://www.asciitable.com.
    - ``f('hello') -> 532``
    - ``f('world') -> 552``
    - ``f('20') -> 98``
    - ``f('player') -> 653``
    - ``f('replay') -> 653`` Note how two different words like ``player`` and ``replay`` produce the same hash in this case.
4. ``f(key) -> order(key[0]) + 2 * order(key[1]) + 3 * order(key[2]) + ...`` This hash function again uses the order of the
characters but in a weighted manner: the weight of the second character is double, of the third it is triple, etc.
    - ``f('hello') -> 1617``
    - ``f('world') -> 1615``
    - ``f('20') -> 146``
    - ``f('player') -> 2292``
    - ``f('replay') -> 2295`` Note that in this case, anagrams like ``player`` and ``replay`` produce different hash values.

## Exercises

For each of the above algorithms, implement a function to realize the corresponding functionality.
Specifically, for each of the 4 Python files, edit their ``hash`` function to pass the tests.

As is, the hash functions return ``0``, so the built-in tests ``FAIL``. For example, the ``hash1()`` in the [hash1.py](hash1.py)
file produces the following output:

```text
Testing hash1() ...
hello..... FAIL :-( 0 ≠ 1
world..... FAIL :-( 0 ≠ 1
20........ FAIL :-( 0 ≠ 1
player.... FAIL :-( 0 ≠ 1
replay.... FAIL :-( 0 ≠ 1
```

When their hash function is correctly implemented, they ``PASS`` the tests.
For example, when ``hash4()`` is correctly implemented in the [hash4.py](hash4.py) file, it should produce the following output:

```text
Testing hash4() ...
hello..... PASS :-) 1617 = 1617
world..... PASS :-) 1615 = 1615
20........ PASS :-) 146 = 146
player.... PASS :-) 2292 = 2292
replay.... PASS :-) 2295 = 2295
```

Implement the 4 hash functions so that they ``PASS`` their tests:
- ``hash1(key)`` in [hash1.py](hash1.py)
- ``hash2(key)`` in [hash2.py](hash2.py)
- ``hash3(key)`` in [hash3.py](hash3.py)
- ``hash4(key)`` in [hash4.py](hash4.py))
