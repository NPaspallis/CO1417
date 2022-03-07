# This sample Python program experiments with different hashing functions

test_keys = ['hello', 'world', '20', 'player', 'replay']
hash_values_4 = [1617, 1615, 146, 2292, 2295]


# TODO Implement this hash function so that it returns the weighted sum of the order of the key characters.
# Again, use the 'ord' function which takes as argument a character and returns an integer.
# The returned integer corresponds to the index of that character in the ASCII table: https://www.asciitable.com/
# For example, ord('a') -> 97, and ord('A') -> 65
# The result will be: 1 * ord(key[0]) + 2 * ord(key[1]) + 3 * ord(key[2]) + ...
def hash4(key):
    return 0


# This function calls and tests the above hash functions. Do not modify the below code.
def main():
    num_of_keys = len(test_keys)  # total number of test keys

    print('Testing hash4() ...')
    for i in range(num_of_keys):
        key = test_keys[i]  # for the given key ...
        expected_hash = hash_values_4[i]  # ...this is the expected hash ...
        computed_hash = hash4(key)  # ... this is the computed hash ...
        if computed_hash == expected_hash:  # do they match?
            print('%s PASS :-) %s = %s' % (key.ljust(10, '.'), computed_hash, expected_hash))
        else:
            print('%s FAIL :-( %s ≠ %s' % (key.ljust(10, '.'), computed_hash, expected_hash))
    print()  # blank line


main()
