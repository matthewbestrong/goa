def find_hello_index(string):
    index = string.lower().find('hello')
    if index != -1:
        print(f"The word 'hello' starts at index {index}.")
    else:
        print("The word 'hello' was not found in the string.")

# Example usage
string = "Hello there! How are you? Hello again!"
find_hello_index(string)
