from array import *
arr1 = array("i", [1,2,3,4,5,6])

# # 1. create an array and traverse
# for i in arr1:
#     print(i)
# print()
#
# # 2. Access individual elements through indexes
# print(arr1[0])
# print(arr1[1])
# print()
#
# for i, n in enumerate(arr1):
#     print(i, arr1[i], n)

# 3. Append any value to the array using append() method
arr1.append(77)
print(arr1)

# 4. Insert value in an array using insert() method
arr1.insert(3, 17)
print(arr1)

# 5. Extend python array using extend() mehtod
arr2 = [999,888,777,666,555,444]
arr1.extend(arr2)
print(arr1)

# 6. Add items from list into array using fromlist() method
temp_list = [20,21,22]
arr1.fromlist(temp_list)
print(arr1)

# 7. Remove any array element using remove
arr1.remove(888)
print(arr1)

# 8. Remove last array element using pop() mehtod
last_num = arr1.pop()
print(last_num)
print(arr1)

# 9. Fetch any element through its index using index() method
num = arr1.index(999)
print(num)

# 10. reverse a puthon array using reverse() method
arr1.reverse()
print(arr1)

# 11. get array buffer information through buffer_info() method
print(arr1.buffer_info())
print()

# 12. Check for number of occurrences of an element using count() method
print(arr1.count(555))

# 13. Convert array to string using tostring() method
# str_temp = arr1.tostring()
# print(str_temp)
# This was depricated in python 3.90 and later

# 14. Convert array to a python list with same elements using tolist() method
print(type(arr1))
lst = arr1.tolist()
print(lst)
print(type(lst))

# 15. Append a string to char array using fromstring() method
# This was depricated in python 3.90 and later

# 16. Slice Elements from an array
slice = arr1[4:9]
print(slice)
