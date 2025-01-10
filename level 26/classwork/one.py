def manual_len(input_list):
    """
    This function calculates the length of a list without using the built-in len() function.
    """
    count = 0  # Variable to store the length
    for _ in input_list:  # Iterating over the list
        count += 1
    return count

# Example usage
my_list = [1, 2, 3, 4, 5]
length = manual_len(my_list)
print(f"The length of the list is: {length}")

# Testing with different lists
print(manual_len([]))  # Empty list
print(manual_len([10, 20, 30, 40]))  # List with 4 elements
print(manual_len(["a", "b", "c", "d", "e", "f"]))  # List with strings
