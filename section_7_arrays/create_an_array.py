from array import *

arr1 = array("i", [1,2,3,4,2,6])
arr2 = array("d", [1.3,1.5,1.6,9])

print(arr1)
# print(arr2)
arr2.append(11)
# print(arr2)

arr1.insert(2,7)
# print(arr1)
#
# def traverse_array(array):
#     for i in array:
#         print(i)
#
# traverse_array(arr1)
# ----------------------------------------------------------------------
# def access_element(array, index):
#     if index > len(array):
#         print("That index does not exist in this array.")
#     else:
#         print(array[index])
#
# access_element(arr1, 10)

# ----------------------------------------------------------------------
# Finding an element

# def search_in_array(array, value):
#     for i in array:
#         if i == value:
#             return array.index(value)
#     return "The element doesn't exist in the array."
#
# print(search_in_array(arr1, 2))

# ----------------------------------------------------------------------
# Delete an element
# print(arr1)
# arr1.remove(7)
# print(arr1)

# ----------------------------------------------------------------------

