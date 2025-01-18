def verify_uppercase():
    string = input("Enter a string: ")
    if string.isupper():
        print("The string contains only uppercase letters.")
    else:
        print("The string does not contain only uppercase letters.")

# Example usage
verify_uppercase()
