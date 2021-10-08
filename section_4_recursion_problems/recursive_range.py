def recursiveRange(num):
    assert num >= 0 and int(num) == num, "num needs to be a positive integer"
    if num == 0:
        return 0
    else:
        return num + recursiveRange(num-1)

print(recursiveRange(6))