def decimal_to_binary(n):
    assert int(n) == n, "n must be an integer only"
    if n < 0:
        n *= -1
    if n == 0:
        return 1
    else:
        return n%2 + 10 * decimal_to_binary(int(n/2))

print(decimal_to_binary(-10))