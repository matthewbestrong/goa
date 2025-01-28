# Function to append all elements of one list to another list
def append_lists(list1, list2):
    list1.extend(list2)  # Append all elements of list2 to list1
    return list1

# Function to insert an item at a specified index
def insert_item_at_index(lst, index, item):
    lst.insert(index, item)  # Insert the item at the specified index
    return lst

# Function to insert an item at the beginning of a list
def insert_at_beginning(lst, item):
    lst.insert(0, item)  # Insert the item at the beginning of the list
    return lst

# Function to insert an item at the end of a list using insert method
def insert_at_end(lst, item):
    lst.insert(len(lst), item)  # Insert the item at the end of the list
    return lst

# Example usage:

# 1. Append all elements of list2 to list1
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = append_lists(list1, list2)
print("After appending:", result)  # Output: [1, 2, 3, 4, 5, 6]

# 2. Insert an item at a specified index
index = 2
item = 7
result = insert_item_at_index(result, index, item)
print("After inserting at index:", result)  # Output: [1, 2, 7, 3, 4, 5, 6]

# 3. Insert an item at the beginning of the list
item = 0
result = insert_at_beginning(result, item)
print("After inserting at the beginning:", result)  # Output: [0, 1, 2, 7, 3, 4, 5, 6]

# 4. Insert an item at the end of the list
item = 8
result = insert_at_end(result, item)
print("After inserting at the end:", result)  # Output: [0, 1, 2, 7, 3, 4, 5, 6, 8]
