def factorial(num):
    assert num>=0 and int(num) == num, "num must be a positive integer"
    if num in [0,1]:
        return 1
    return num * factorial(num-1)

print(factorial(3))