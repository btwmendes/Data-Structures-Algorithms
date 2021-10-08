def fibonacci(n):
    """n is the index in the fibonacci sequence."""
    assert n >= 0 and int(n) == n, 'The number must be a positive integer only'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(11))