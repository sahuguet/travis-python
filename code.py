"""Example Google style docstrings.

This module demonstrates documentation as
"""

memoizeMap = {}

"""This is a bad-ass memoized fibonacci sequence generator
"""

def fibonacci(val):

    if val not in memoizeMap:
        if val == 0:
            memoizeMap[val] = 0
        elif val == 1:
            memoizeMap[val] = 1
        else:
            memoizeMap[val] = fibonacci(val-2) + fibonacci(val-1)

    return memoizeMap[val]

def fibonacciSeries(val):
    return [fibonacci(x) for x in range(0, val)]

def main():
    for x in fibonacciSeries(150):
        print x

if __name__ == "__main__":
    main()
