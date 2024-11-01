# TASK 1
#
# FIBONACCI GENERATOR
#
# The Fibonacci series is a sequence where each number is
# the sum of the two preceding numbers, defined by a
# mathematical recurrence relationship.
# (0,) 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ......
# Note: The zero is sometimes not mentioned.


def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return  fibonacci(i-2) + fibonacci(i-1)

for x in range(13):
    print(fibonacci(x))