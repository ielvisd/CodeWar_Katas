""" Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24 """


def grow(arr):

    # Initializes result as 1
    result = 1
    # Sets the result equal to the value of multiplying all the values in the array together
    for num in arr: 
      result *= num

    return result

print(grow([1, 2, 3, 4]))

# test.describe("Example Tests")
# tests = [
#     [6 , [1, 2, 3]],
#     [16, [4, 1, 1, 1, 4]],
#     [64, [2, 2, 2, 2, 2, 2]],
# ]

# for exp, inp in tests:
#     test.assert_equals(grow(inp), exp)

# Best Practice Solutions

# def grow(arr):
#     return reduce(lambda x, y: x * y, arr)

# from functools import reduce
# from operator import mul

# def grow(arr):
#     return reduce(mul, arr, 1)