import hashlib

test_keys = ['hello', 'world', '20', 'player', 'replay']
hash_values_sha256 = ["2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
                      "486ea46224d1bb4fb680f34f7c9ad96a8f24ec88be73ea8e5a6c65260e9cb8a7",
                      "f5ca38f748a1d6eaf726b8a42fb575c3c71f1864a8143301782de13da2d9202b",
                      "cdb59355f3ba293977fc0945fb85f11822d412c45c7520c7121bd2234f6c1f48",
                      "ac203c9843b5bd8c883e07039ff82820c94422010be6108bb82403ca25376a22"]


# TODO Implement this hash function so that it returns the correct SHA256 hash
def sha256(key):
    return 0


# This function calls and tests the above hash functions. Do not modify the below code.
def main():
    num_of_keys = len(test_keys)  # total number of test keys

    print('Testing hash1() ...')
    for i in range(num_of_keys):
        key = test_keys[i]  # for the given key ...
        expected_hash = hash_values_sha256[i]  # ...this is the expected hash ...
        computed_hash = sha256(key)  # ... this is the computed hash ...
        if computed_hash == expected_hash:  # do they match?
            # prints PASS message ('ljust' adds padding up to 10 chars using dots)
            print('%s PASS :-) %s = %s' % (key.ljust(10, '.'), computed_hash, expected_hash))
        else:
            print('%s FAIL :-( %s ≠ %s' % (key.ljust(10, '.'), computed_hash, expected_hash))


main()
