def manual_range(start, end, step):
    """
    This function generates a range of numbers based on the given start, end, and step.
    It iterates through the range and prints only even numbers.
    """
    # Generate the range using a list comprehension
    range_list = list(range(start, end, step))
    
    # Iterate through the range and print only even numbers
    for number in range_list:
        if number % 2 == 0:
            print(number)

# Example function calls
manual_range(0, 10, 1)
print("---")
manual_range(5, 20, 2)
print("---")
manual_range(10, 0, -2)
print("---")
manual_range(-10, 10, 3)
print("---")
manual_range(2, 22, 4)
