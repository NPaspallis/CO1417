import hashlib
import time

LOOPS = 1000000

start = time.perf_counter()  # time at this point (begin measuring)
for int in range(LOOPS):
    hashlib.md5("hello".encode('utf-8')).hexdigest()
end = time.perf_counter()  # time at this point (end measuring)
delta = end - start  # the difference of 'begin' and 'end', in seconds
print("MD5 time: %f" % delta)

start = time.perf_counter()  # time at this point (begin measuring)
for int in range(LOOPS):
    hashlib.sha256("hello".encode('utf-8')).hexdigest()
end = time.perf_counter()  # time at this point (end measuring)
delta = end - start  # the difference of 'begin' and 'end', in seconds
print("SHA256 time: %f" % delta)
