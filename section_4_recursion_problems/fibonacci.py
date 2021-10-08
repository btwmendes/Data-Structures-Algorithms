def fib(num):
    assert num>=0 and int(num) == num, "num needs to be a positive integer"
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)

print(fib(35))