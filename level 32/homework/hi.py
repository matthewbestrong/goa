def append_items_to_list(original_list, items_to_append):
    """
    Appends each item from items_to_append to the original_list.

    Parameters:
    original_list (list): The list to which items will be appended.
    items_to_append (list): The list of items to append to the original list.

    Returns:
    None
    """
    original_list.extend(items_to_append)

# Example usage:
my_list = [1, 2, 3]
new_items = [4, 5, 6]
append_items_to_list(my_list, new_items)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
