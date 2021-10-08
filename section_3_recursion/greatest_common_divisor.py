def gcd(a,b):
    assert int(a) == a and int(b) == b, "a and b must be integers greater than zero"
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

print(gcd(48, -18))