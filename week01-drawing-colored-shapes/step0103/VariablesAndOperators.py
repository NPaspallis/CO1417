# In this exercise, we will familiarize with variables and operators.

# In python, you can declare variables simply by using a new name and assigning it a value.
# The type of the variable is implied by the assigned value.
# For example, in the below we declare two variables, 'w' and 'h', both integers, initialized to 800 and 500
# respectively.
w = 800
h = 400

# Note how you can concatenate values of different types into strings, using commas.
print("width, height: ", w, ", ", h)
print()  # prints empty line

# You can also concatenate strings using '+', but you need to manually convert non strings to strings using the 'str'
# function.
print("width, height: " + str(w) + ', ' + str(h))
print()  # prints empty line

# Of course, variables can 'vary' (i.e. be modified in runtime). Meaning you can assign a new value whenever you want.
h = 500
print("h: ", h)
print()  # prints empty line

# You can use the standard numeric operators: +, -, *, / , % which behave more or less like in Java.
# You can even use the unary operators +=, -=, *=, /=, %= with functionality also similar to Java.
h += 100
print("h: ", h)
print()  # prints empty line

# You can also define Boolean values, using the 'True' and 'False' literals.
# You can use the logical operators: 'and', 'or', and 'not'. For example, assuming 'weekend = True' and
# 'bank_holiday = False', we can use an expression like the following to determine if we go to work:
# 'work_day = not weekend and not bank_holiday'
b = True
c = True and False
print('b: ', b, ', c:', c)  # This prints 'b:  True , c: False'
print()  # prints empty line

# More exhaustively, the Logical table for 'and' is:
print('Logical table for \'and\'')  # Note you can use the backslash as an escape character, similar to Java.
print('False and False -> ' + str(False and False))
print('False and True  -> ' + str(False and True))
print('True  and False -> ' + str(True and False))
print('True  and True  -> ' + str(True and True))
print()  # prints empty line

# And similarly, the Logical table for 'or' is:
print('Logical table for \'or\'')
print('False or False -> ' + str(False or False))
print('False or True  -> ' + str(False or True))
print('True  or False -> ' + str(True or False))
print('True  or True  -> ' + str(True or True))
print()  # prints empty line

# Finally, the Logical table for 'not' (a unary operator) is:
print('Logical table for \'not\'')
print('not False -> ' + str(not False))
print('not True  -> ' + str(not True))
print()  # prints empty line

# You can learn all about Python operators at: https://www.w3schools.com/python/python_operators.asp

# Strangely, Python has no built-in keyword for defining 'constants'. Instead you are advised to use ALL CAPS to signify
# a constant (even though in reality you can still change such value and the compiler will not warn you :-( ...)

TITLE = 'Hello World!'  # Remember, you can define strings using 'single quotes' or "double quotes" -- both are ok.
WIDTH = 800
HEIGHT = 600

# todo Run this program and note the output in the console. Verify that it is as expected.
