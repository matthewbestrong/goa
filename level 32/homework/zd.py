def append_to_list(existing_list, item):
    """
    Appends an item to the end of the provided list.

    Parameters:
    existing_list (list): The list to which the item will be appended.
    item: The item to append to the list.

    Returns:
    None
    """
    existing_list.append(item)

# Example usage:
my_list = [1, 2, 3]
append_to_list(my_list, 4)
print(my_list)  # Output: [1, 2, 3, 4]
