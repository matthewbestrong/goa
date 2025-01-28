def csv_to_list(csv_string):
    """
    Converts a comma-separated string into a list of individual items.

    Parameters:
    csv_string (str): The CSV string to convert.

    Returns:
    list: A list containing the individual items from the CSV string.
    """
    # Use the split() method to divide the string by commas
    items = csv_string.split(',')
    return items

# Example usage:
csv_string = "apple,banana,cherry,dates"
item_list = csv_to_list(csv_string)
print(item_list)
