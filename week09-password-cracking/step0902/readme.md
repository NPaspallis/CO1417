# Hashing: MD5 and SHA256

Building *good* hashing algorithms is not easy.
Thankfully, there exist many good hashing algorithms available, and in most cases these are readily available
in Python (and in other platforms) via libraries.

### MD5

One of the most popular hash functions was [MD5](https://en.wikipedia.org/wiki/MD5).
Perhaps you're more familiar with MD5 digests, which are used as checksums to verify data integrity. For example,
when you download a large file from the Internet, like a DVD-image which can be 4-5 GB, you can use MD5 to verify
that no errors occurred in the transmission.

The MD5 algorithm, and other hash functions, are readily available in Python via the ``hashlib`` library.
To use it, you must first ``import`` that library.

Example of using MD5 in Python:

```python
import hashlib

print("hello -> ", hashlib.md5("hello".encode('utf-8')).hexdigest())
```

This generates the following output:
```text
hello ->  5d41402abc4b2a76b9719d911017c592
```

Note how the result is not an integer number anymore. As MD5 produces a 128-bit long hash value, it is often
represented with its [Hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) equivalent which is a bit more compact to express.
Specifically, it takes 32 Hex digits to represent a 128-bit sequence (4-bits per Hex digit).

        Today, MD5 is considered ineffective, as it weas cryptographically broken.
        While it is still used for data integrity checks, it is effective only against unintentional corruption.

More effective hashing functions exist and are used for cryptography and data integrity purposes. 

### SHA256

The SHA (*Secure Hash Algorithm*) family of cryptographic functions is widely used in cryptography.

The SHA256 is so-named because it produces a 256-bit long hash value. In its Hexadecimal form, it takes 64 Hex digits.

Example of using SHA256 in Python:

```python
import hashlib

print("hello -> ", hashlib.sha256("hello".encode('utf-8')).hexdigest())
```

This generates the following output:
```text
hello ->  2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

## Exercises

Implement the corresponding hashing function for MD5 and SHA256. Use the ``hashlib`` library.

Implement the 2 hash functions so that they ``PASS`` their tests:
- ``md5(key)`` in [check_md5.py](check_md5.py)
- ``sha256(key)`` in [check_sha256.py](check_sha256.py)
