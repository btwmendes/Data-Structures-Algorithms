from array import *

arr1 = array("i", [1,2,3,4,5,6])
arr2 = array("d", [1.3,1.5,1.6,9])

print(arr1)
print(arr2)
arr2.append(11)
print(arr2)

arr1.insert(2,7)
print(arr1)

def traverse_array(array):
    for i in array:
        print(i)

traverse_array(arr1)