# This sample Python program experiments with different hashing functions

test_keys = ['hello', 'world', '20', 'player', 'replay']
hash_values_1 = [1, 1, 1, 1, 1]


# TODO Implement this hash function so that it always return the same hash (i.e., 1).
def hash1(key):
    return 0


# This function calls and tests the above hash functions. Do not modify the below code.
def main():
    num_of_keys = len(test_keys)  # total number of test keys

    print('Testing hash1() ...')
    for i in range(num_of_keys):
        key = test_keys[i]  # for the given key ...
        expected_hash = hash_values_1[i]  # ...this is the expected hash ...
        computed_hash = hash1(key)  # ... this is the computed hash ...
        if computed_hash == expected_hash:  # do they match?
            # prints PASS message ('ljust' adds padding up to 10 chars using dots)
            print('%s PASS :-) %s = %s' % (key.ljust(10, '.'), computed_hash, expected_hash))
        else:
            print('%s FAIL :-( %s ≠ %s' % (key.ljust(10, '.'), computed_hash, expected_hash))


main()
