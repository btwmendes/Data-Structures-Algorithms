def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not (cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True


def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True