# Playing with Lists

Lists are some of the most common and useful data structures in Python.

In this step, we cover several tasks and their implementation in Python using Lists.

### Basic tasks

#### 1. Printing a List

Simply pass a list as argument in the ``print`` function to print it.

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(letters)  # prints: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
```

#### 2. Selecting an item in a List 

You can specify the index of the item to be selected. Remember that items in a list are zero-indexed!
```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# select the 'e', i.e. the 5th element in the 'letters' list
print(letters[4])  # why select index 4 and not 5?
```

#### 3. Selecting a subrange of a List 

In Python it is possible to select a subrange of a list, using the ``:`` operator. The returned value is another list.

Note that the _from_ index is included and _to_ index is not. 

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
some_letters = letters[1:4]  # selects the items at indices 1, 2, 3 (not 4)
print(some_letters)  # prints ['b', 'c', 'd']
```

#### 4. Selecting a subrange of a List, using steps

It is also possible to add a third parameter to indicate the step between indices. For example, the selection
``[f:t:s]`` selects all indices from ``f`` until before ``t``, with a step of ``s``. 

You can leave some of the ``from`` or the ``to`` indices empty to indicate the _beginning_ and the _end_ of the list.
For example, the selection ``[::2]`` means select every second item in the list, i.e. at index 0, 2, 4, etc.

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
spaced_letters = letters[1:8:2]  # selects the items at indices 1, 3, 5, 7 (not 8)
print(spaced_letters)  # prints ['b', 'd', 'f', 'h']
all_spaced_letters = letters[::2]  # selects all the items at indices 0, 2, 4, 6, 8, with a step of 2
print(all_spaced_letters)  # prints ['a', 'c', 'e', 'g', 'i']
```

#### 5. Using a negative step

You set the step to a negative number to, to go through the items in reverse order. For example, the selection
``[10:5:-2]`` means select the items in the list from index 10, down to before 5, moving back 2 positions each time,
i.e. indices ``10, 8, 6``.

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
some_reversed_letters = letters[6:3:-1]  # selects the items from index 6 down to before 3
print(some_reversed_letters)  # prints ['g', 'f', 'e']
reversed_letters = letters[::-1]  # selects all the items, in reverse order
print(reversed_letters)  # prints ['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
```

#### 6. Sort, Shuffle, and Reverse a List in place

It is possible to apply any of the ``sort``, ``shuffle``, and ``reverse`` functions on a List.

```python
import random  # required for the 'random.shuffle(...)' function
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
letters.reverse()  # note that this approach reverses the list 'in place' meaning the original list is modified
print(letters)  # prints ['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
random.shuffle(letters)  # shuffles the given list
print(letters)  # prints ['c', 'b', 'h', 'f', 'e', 'd', 'j', 'i', 'a', 'g'] (or another shuffled version of the list)
letters.sort()  # sorts this list
print(letters)   # prints ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
```

### Using List Comprehension

Python has a feature called [List Comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp).
Using this feature, it is possible to produce a new list by iterating, filtering, and modifying the elements of an
existing list. For example, given a list of numbers such as ``[1, 2, 3, ...]`` it is possible to produce one with the
squares of the corresponding numbers, i.e. ``[1, 4, 9, ...]``.

See the following examples for more details.

#### 7. Given a list of numbers, produce a new list containing the square of each item

The straightforward way to solve this problem is to use a loop to iterate each item in the given list and compute its
square, inserting it into a new list.

```python
numbers = [1, 2, 3, 4, 7, 10, 12, 20]
print(numbers)
squares = []  # initially empty
for n in numbers:
    squares.append(n*n)  # add the square of each number to the 'squares' list
print(squares)  # [1, 4, 9, 16, 49, 100, 144, 400]
```

Using List Comprehension it is possible to do this using a more succinct way:

```python
numbers = [1, 2, 3, 4, 7, 10, 12, 20]
squares2 = [n*n for n in numbers]  # compute the 'n*n' value of each value 'n' in list 'numbers'
print(squares2)  # [1, 4, 9, 16, 49, 100, 144, 400]
```

#### 8. Select all words which contain the letter 'a'

When you need to check if a condition applies for each item in a list, you normally need to run a loop and do the check
for each item.
For example, to seelct all words containing letter ``'a'`` you can use a loop as follows:

```python
sweets = ['apple pie', 'biscuit', 'cupcake', 'donut', 'eclair', 'froyo', 'gingerbread', 'honeycomb', 'ice cream', 'jelly']
sweets_with_a = []  # initially empty list
for s in sweets:
    if 'a' in s:  # check if letter 'a' is contained in string s
        sweets_with_a.append(s)
print(sweets_with_a)  # prints ['apple pie', 'cupcake', 'eclair', 'gingerbread', 'ice cream']
```

Using List Comprehension it is possible to do this using a more succinct way:

```python
sweets = ['apple pie', 'biscuit', 'cupcake', 'donut', 'eclair', 'froyo', 'gingerbread', 'honeycomb', 'ice cream', 'jelly']
sweets_with_b = [s for s in sweets if 'b' in s]  # select item s for all items in sweet if 'b' is contained in s
print(sweets_with_b)  # prints ['biscuit', 'gingerbread', 'honeycomb']
```

#### 9. Compute the prime numbers in the range 1..100

Study the following code used to compute if a number is [prime](https://en.wikipedia.org/wiki/Prime_number) or not:

```python
import math
def is_prime(x):
    """ Returns True if the given number is prime, False otherwise """
    if x <= 1: # one, zero and negative numbers are not prime
        return False
    if x == 2:
        return True
    for n in range(2, math.isqrt(x) + 1): # isqrt returns the floor int of the square root, i.e. isqrt(10) -> 3
        if x % n == 0:
            return False
    return True
```

While this function is not optimal, it is simple enough for our demo.

To compute all prime numbers in the range 1..100 it is sufficient to run a loop and check for each value:

```python
primes = []  # initially empty
for x in range(1,100):
    if is_prime(x):
        primes.append(x)
print(primes)  # prints [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] 
```

This code can be further simplified using List Comprehension. The filtering can be applied using the ``is_prime`` function.

```python
primes = [x for x in range(1, 100) if is_prime(x)]
print(primes)  # prints [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

### 10. Remove empty strings from a list of strings

Assume you have a list of possibly empty names, such as ``["Mike", "", "Emma", "Kelly", "", "Brad"]``.
You can filter out selected values such as the empty strings using the ``filter`` function.

        Note that the 'filter' function returns an iterator. You can force it to produce a list using the 'list' constructor.

In the following example, the code filters out the values matching the ``None`` keyword, i.e. empty strings.

```python
names = ["Mike", "", "Emma", "Kelly", "", "Brad"]
names1 = list(filter(None, names))
print(names1)  # prints ['Mike', 'Emma', 'Kelly', 'Brad']
```

Another way to achieve the same result is to use List Comprehension again:

```python
names = ["Mike", "", "Emma", "Kelly", "", "Brad"]
names2 = [name for name in names if name != '']  # for each name in the list, select those which are not equal to '' (empty)
print(names2)  # prints ['Mike', 'Emma', 'Kelly', 'Brad']
```
