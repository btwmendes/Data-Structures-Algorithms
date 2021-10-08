def power(base, exponent):
    assert int(exponent) == exponent and exponent>=0, "exponent must be an integer greater or equal to zero"
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    return base * power(base, exponent-1)

print(power(4, 3))