import numpy as np

letters = ["a", "b", "c", "d", "e"]

my_array = np.array([[1,2,3,4,5], letters, [12,17,12,8,6], [15,18, 14,9,8]])
print(my_array)
print()
print(my_array[0][1])
# slice is rows then columns

print(my_array[3][0])
print()

# ---------------------------------------------------------------
# insertion or adding values
# add columns
new_array = np.insert(my_array, 0, [[5,4,3,2]], axis=1)
print(new_array)
print()

new_array_2 = np.insert(new_array,2,[[66,77,88,99,11,22]], axis=0)
print(new_array_2)
print()

new_array_2 = np.append(new_array,[[66,77,88,99,11,22]], axis=0)
print(new_array_2)

# ---------------------------------------------------------------
# # accessing elements
# def access_elements(array, row_index, column_index):
#     print(array[row_index][column_index])
#
# access_elements(new_array,2,2)

# ---------------------------------------------------------------
# traverse two dimensional array

# def traverse_array(array):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             print(array[i][j])
#
# traverse_array(new_array_2)

# ---------------------------------------------------------------
# searching two dimensional array
# def search_arrray(array, value):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             if array[i][j] == value
#                 print(array[i][j])
#                 return f"The value is located at index {i} {j}"
#             else:
#                 return "The element is not found"
#
# print(search_arrray(my_array, 14))

# for row in my_array:
#     for num in row:
#         print(type(num))

# ---------------------------------------------------------------
# deletion two dimenstional array
new_td_array = np.delete(new_array_2, 0, axis=0)
print()
print(new_td_array)