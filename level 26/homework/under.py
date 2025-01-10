def even_or_odd(number):
    """
    This function determines whether a given integer is even or odd.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
num = int(input("Enter an integer: "))
result = even_or_odd(num)
print(f"The number {num} is {result}.")
