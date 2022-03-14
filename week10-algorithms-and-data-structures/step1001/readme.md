# Data Structures in Python

This week we cover important data structures and algorithms, and their application using Python.

## Data Structures

A *Data Structure* is a particular way to store and organise data in a computer system, so it can be used effectively.

In its simplest form, a data structure can consist of a single primitive data type, such as an Integer or Floating-point
number, or a Boolean, or a String.

More complex concepts, such as a _mailing address_ (e.g., UCLan Cyprus' address is ``12-14 Univ. Avenue, Pyla, 7080,
Cyprus``) might require a combination of different primitive data types, such as an Integer for the postal code, a
String for the street name and number, etc.

### Dealing with collections of data

One of the main advantages of working with computer systems is their ability to handle large quantities of data, aka
_Collections_.
For example, you could consider a collection of numbers to represent the temperature in Nicosia over the past 10 years.
Or you could consider a collection containing all the capitals in the world.

```python
temperatures = [14, 15, 15, 14, 16, 17, 17, 15, 16, ..., 18, 17, 15, 18, 18]
capitals = ['Abu Dhabi', 'Abuja', 'Athens', ..., 'London', 'Nicosia', ..., 'Zagreb']
```

Python offers 4 main constructs for dealing with data _collections_:

#### Lists

The most common data structure is the List, which is essentially a sequence of values (of any type).
The main characteristics of Lists are:
- they are ordered,
- they are editable, and
- they allow multiple copies of the same value.

You can learn more at: https://www.w3schools.com/python/python_lists.asp.

        Python does not include a concept of Arrays. But the Lists is an efficient and effective substitute.

Carefully read the following code snippets using Lists:

```python
list1 = [1, 2, 3]  # initialize a list using the square brackets notation
list2 = list([2, 1, 3])  # equivalent to 'list2 = [2, 1, 3]'
print(list1 == list2)  # prints 'False' because lists are ordered
list3 = [1, 1, 2, 3]  # valid because lists allow multiple copies of the same value
list4 = [1, 2]
list4.append(3)  # results to list4 being equal to [1, 2, 3]
print(list1 == list4)  # prints 'True' because list1 and list4 both equal to [1, 2, 3]
list5 = [1, 2, True, 'Some Words', 5, False]  # a list can contain values of different types
```

#### Tuples

A Tuple is another data structure. It represents unordered, unmodifiable collections.
The main characteristics of Tuples are:
- they are ordered (like Lists),
- they are unchangeable (unlike Lists), and
- they allow multiple copies of the same value (also like Lists).

You can learn more at: https://www.w3schools.com/python/python_tuples.asp.

Carefully read the following code snippets using Tuples:

```python
tuple1 = ('hello', 'world')  # initialize a tuple using the round brackets notation
tuple2 = tuple(('world', 'hello'))  # equivalent to 'tuple2 = ('world', 'hello')'
print(tuple1 == tuple2)  # prints 'False' because tuples are ordered
tuple3 = (1, 1, 2, 3)  # valid because tuples allow multiple copies of the same value
print(tuple1 == ('hello', 'world'))  # prints 'True' because tuple1 equals to ('hello', 'world')
tuple4 = [1, 2, True, 'Some Words', 5, False]  # a tuple can contain values of different types
tuple5 = (1, 2)
tuple5.append(3)  # ERROR! tuples CANNOT be modified
```

#### Sets

A Set is a data structure which represents unordered collections of non-repeating values.
The main characteristics of Sets are:
- they are not ordered (unlike Lists and Tuples),
- they are changeable (like Lists and unlike Tuples), and
- they do not allow multiple copies of the same value (unlike Lists and Tuples).

You can learn more at: https://www.w3schools.com/python/python_sets.asp.

Carefully read the following code snippets using Sets:

```python
set1 = {'hello', 'world'}  # initialize a set using the curly brackets notation
set2 = set({'world', 'hello'})  # equivalent to 'set2 = {'world', 'hello'}'
print(set1 == set2)  # prints 'True' because sets are unordered
set3 = {1, 1, 2, 3}  # the second '1' value is ignored because sets do not allow multiple copies of the same value
print(set3)  # prints {1, 2, 3}
print(set1 == {'hello', 'world'})  # prints 'True' because set1 equals to {'hello', 'world'} (as well as to {'world', 'hello'})
set4 = {1, 2, True, 'Some Words', 5, False}  # a set can contain values of different types
set5 = {1, 2}
set5.add(3)  # valid - the result is set5 being equal to {1, 2, 3}
```

#### Dictionaries.

A Dictionary is a handy data structure which represents ``key: value`` pairs.

The main characteristics of Dictionaries are:
- they are ordered (like Lists and Tuples, unlike Sets),
- they are changeable (like Lists and Sets, unlike Tuples), and
- they do not allow multiple copies of the same ``key: value`` pair.

        As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

You can learn more at: https://www.w3schools.com/python/python_dictionaries.asp.

Carefully read the following code snippets using Dictionaries:

```python
dict1 = {'key1': 'hello', 'key2': 'world'}  # initialize a dict using the curly brackets notation, and a sequence of key:value pairs
dict2 = dict({'key2': 'world', 'key1': 'hello'})  # equivalent to 'dict2 = {'key2': 'world', 'key1': 'hello'}'
print(dict1 == dict2)  # prints 'True' because dicts are unordered
dict3 = {1: 'some value', 2: 'another value', 2: 'different value'}  # each key must be unique - one of the two keys is overwritten
print(dict3)  # prints {1: 'some value', 2: 'different value'}
print(dict1 == {'key1': 'hello', 'key2': 'world'})  # prints 'True' because dict1 equals to {'key1': 'hello', 'key2': 'world'} (as well as to {'key2': 'world', 'key1': 'hello'})
dict4 = {1: 'One', 2: 'Two', 'key': 'a value', 'other key': False}  # a dict can contain values of different types - keys must be numbers or strings though
dict5 = {'One': 'Uno', 'Two': 'Dos'}
print(dict5['One'])  # prints 'Uno' - the dict values can be accessed using the square brackets to specify the desired key
dict5['Three'] = 'Tres'  # valid - the result is dict5 being updated to {'One': 'Uno', 'Two': 'Dos', 'Three': 'Tres'}
```

## Next step

Study the differences of ``lists``, ``tuples``, ``sets``, and ``dicts`` at
[https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python](https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python).

Then proceed to [step1002](../step1002/readme.md).
