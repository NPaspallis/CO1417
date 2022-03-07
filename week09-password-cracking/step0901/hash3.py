# This sample Python program experiments with different hashing functions

test_keys = ['hello', 'world', '20', 'player', 'replay']
hash_values_3 = [532, 552, 98, 653, 653]


# TODO Implement this hash function so that it returns the sum of the order of the key characters.
# You can use the 'ord' function which takes as argument a character and returns an integer.
# The returned integer corresponds to the index of that character in the ASCII table: https://www.asciitable.com/
# For example, ord('a') -> 97, and ord('A') -> 65
# The result will be: ord(key[0]) + ord(key[1]) + ord(key[2]) + ...
def hash3(key):
    return 0


# This function calls and tests the above hash functions. Do not modify the below code.
def main():
    num_of_keys = len(test_keys)  # total number of test keys

    print('Testing hash3() ...')
    for i in range(num_of_keys):
        key = test_keys[i]  # for the given key ...
        expected_hash = hash_values_3[i]  # ...this is the expected hash ...
        computed_hash = hash3(key)  # ... this is the computed hash ...
        if computed_hash == expected_hash:  # do they match?
            print('%s PASS :-) %s = %s' % (key.ljust(10, '.'), computed_hash, expected_hash))
        else:
            print('%s FAIL :-( %s ≠ %s' % (key.ljust(10, '.'), computed_hash, expected_hash))
    print()  # blank line


main()
