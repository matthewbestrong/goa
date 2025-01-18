def verify_lowercase():
    string = input("Enter a string: ")
    if string.islower():
        print("The string contains only lowercase letters.")
    else:
        print("The string does not contain only lowercase letters.")

# Example usage
verify_lowercase()
