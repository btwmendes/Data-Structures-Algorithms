def power(base, exponent):
    assert exponent >= 0 and int(exponent) == exponent, "The exponent must be greater than or equal to zero" \
                                                        " and an integer."
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    else:
        return base * power(base, exponent-1)

print(power(2,.5))