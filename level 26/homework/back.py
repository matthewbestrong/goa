def find_maximum(numbers):
    """
    This function takes a list of numbers as input and returns the maximum value.
    """
    if not numbers:  # Check if the list is empty
        return None
    return max(numbers)

# Example usage
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
maximum = find_maximum(numbers)
if maximum is not None:
    print(f"The maximum value is: {maximum}")
else:
    print("The list is empty. No maximum value.")
