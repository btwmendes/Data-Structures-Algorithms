def factorial(n):
    assert n>=0 and int(n) == n, 'The number must be a positive integer only'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(6))


# def factorial(n):
#     try:
#         if n in [0,1]:
#             return 1
#         else:
#             return n * factorial(n-1)
#     except RecursionError:
#         print("Must use a positive integer")
#         return None
#     except TypeError:
#         print("You have a type error")
#         return None
#
#
# print(factorial(-6))