def productOfArray(arr):
    product = 1
    for num in arr:
        product *= num
    return product

print(productOfArray([1,2,3]))


# Solution
def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])
