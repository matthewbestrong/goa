def sum_of_two_numbers(num1, num2):
    """
    This function takes two numbers as input and returns their sum.
    """
    return num1 + num2

# Example usage
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

result = sum_of_two_numbers(number1, number2)
print(f"The sum of {number1} and {number2} is {result}.")
