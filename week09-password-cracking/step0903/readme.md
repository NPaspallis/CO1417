# Benchmarks

Often you want to measure the performance of algorithms experimentally.
You can do that by measuring the actual time it takes to execute it.

In programming, you can measure the time it takes to run some code by taking the timestamp *before* and
*after* its execution, and computing their difference, i.e., their *delta*.

In Python you can do this as follows:

```python
import time

start = time.perf_counter()  # time at this point (begin measuring)
# put the code to be timed here ...
end = time.perf_counter()  # time at this point (end measuring)
delta = end - start  # the difference of 'begin' and 'end', in seconds
print("elapsed time in seconds: %f" % delta)
```

## Benchmarking the MD5 and SHA256 algorithms

You can use this to *benchmark* algorithms.
For example, to compare the time performance of MD5 and SHA256, we could use an approach as follows:

```python
import hashlib
import time

start = time.perf_counter()  # time at this point (begin measuring)
hashlib.md5("hello".encode('utf-8')).hexdigest()
end = time.perf_counter()  # time at this point (end measuring)
delta = end - start  # the difference of 'begin' and 'end', in seconds
print("MD5 time: %f" % delta)

start = time.perf_counter()  # time at this point (begin measuring)
hashlib.sha256("hello".encode('utf-8')).hexdigest()
end = time.perf_counter()  # time at this point (end measuring)
delta = end - start  # the difference of 'begin' and 'end', in seconds
print("SHA256 time: %f" % delta)

```

This generates the following output:
```text
MD5 time: 0.000013
SHA256 time: 0.000011
```

Unfortunately this is not very helpful. The two times are quite similar, and it's hard to tell if one is indeed faster.

The problem is that the execution of either is relatively very fast and thus hard to compare when we only run them *once*.

## Benchmarking using Loops

A solution is to run each of the measured algorithms *many* times, so we can make a more meaningful comparison.
This can be easily achieved by repeating this a number of times, using loops.

The resulting code is very similar. The only change is the addition of a loop around the measured code:
```python
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
```

The execution of this code produces the following output:
```text
MD5 time: 0.840585
SHA256 time: 0.919724
```

Running this code a number of times, we observe that it consistently produces similar results. This
can give us some confidence that indeed the MD5 is *faster* than SHA256.

### Exercise

- Modify the above code from [benchmark.py](benchmark.py) to run it for different values of LOOPS:
  - 1000
  - 10000
  - 100000
  - 1000000
  - 10000000
- Write down your answers. Is the MD5 consistently faster than SHA256?
