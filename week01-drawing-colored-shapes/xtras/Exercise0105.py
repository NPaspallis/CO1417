# The following function is designed to print 'n' numbers in the range from 'start' to 'end'. However, the program
# fails at runtime.
# Identify the problem and provide a fix. The fix consists of adding just one character.


def print_numbers(start, end, n):
    width = end - start + 1
    for i in range(start, end, width / n):
        print(i)
    print('Printed ', n, ' numbers in the space between ', start, ' and ', end)


print_numbers(1, 100, 10)
