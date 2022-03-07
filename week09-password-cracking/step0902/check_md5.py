import hashlib

test_keys = ['hello', 'world', '20', 'player', 'replay']
hash_values_md5 = ["5d41402abc4b2a76b9719d911017c592",
                   "7d793037a0760186574b0282f2f435e7",
                   "98f13708210194c475687be6106a3b84",
                   "912af0dff974604f1321254ca8ff38b6",
                   "b2dbeb695fa205804b1e5e72650ad2bb"]


# TODO Implement this hash function so that it returns the correct MD5 hash
def md5(key):
    return 0


# This function calls and tests the above hash functions. Do not modify the below code.
def main():
    num_of_keys = len(test_keys)  # total number of test keys

    print('Testing hash1() ...')
    for i in range(num_of_keys):
        key = test_keys[i]  # for the given key ...
        expected_hash = hash_values_md5[i]  # ...this is the expected hash ...
        computed_hash = md5(key)  # ... this is the computed hash ...
        if computed_hash == expected_hash:  # do they match?
            # prints PASS message ('ljust' adds padding up to 10 chars using dots)
            print('%s PASS :-) %s = %s' % (key.ljust(10, '.'), computed_hash, expected_hash))
        else:
            print('%s FAIL :-( %s ≠ %s' % (key.ljust(10, '.'), computed_hash, expected_hash))


main()
