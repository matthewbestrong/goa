def append_lists(list1, list2):
    list1.extend(list2)  # Append all elements of list2 to list1
    return list1
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = append_lists(list1, list2)
print(result)  # Output: [1, 2, 3, 4, 5, 6]
 