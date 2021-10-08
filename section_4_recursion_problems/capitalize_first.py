def capitalizeFirst(arr):
    final_lst = []
    # print(final_lst)
    if len(arr) == 0:
        return final_lst
    final_lst.append(arr[0].title())
    # print(arr[0])
    return final_lst + capitalizeFirst(arr[1:])

print(capitalizeFirst(["taco", "cat", "burger"]))