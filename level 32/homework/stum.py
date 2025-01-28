# Function to append all elements of one list to another list
def append_lists(list1, list2):
    list1.extend(list2)  # Append all elements of list2 to list1
    return list1

# Function to insert an item at a specified index
def insert_item_at_index(lst, index, item):
    lst.insert(index, item)  # Insert the item at the specified index
    return lst

# Example usage:
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Append all elements of list2 to list1
result = append_lists(list1, list2)
print("After appending:", result)  # Output: [1, 2, 3, 4, 5, 6]

# Insert an item at a specified index
index = 2
item = 7
result = insert_item_at_index(result, index, item)
print("After inserting:", result)  # Output: [1, 2, 7, 3, 4, 5, 6]
