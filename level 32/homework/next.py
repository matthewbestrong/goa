def welcome_message(name, age):
    """
    This function takes a user's name and age as input
    and returns a welcome message using an f-string.
    """
    return f"Welcome, {name}! You are {age} years old."

# Example usage:
name_input = input("Enter your name: ")
age_input = int(input("Enter your age: "))

message = welcome_message(name_input, age_input)
print(message)
