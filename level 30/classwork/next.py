def manual_find(main_string, str_to_find):
    """
    Finds the index of the first occurrence of str_to_find in main_string.
    If not found, returns -1.
    """
    # გადამოწმება თითოეულ ინდექსზე
    for i in range(len(main_string) - len(str_to_find) + 1):
        # თუ substring-ს ვპოულობთ
        if main_string[i:i+len(str_to_find)] == str_to_find:
            return i
    # თუ არ მოიძებნა
    return -1

# ფუნქციის ტესტირება
main_string = input("Enter the main string: ")
str_to_find = input("Enter the string to find: ")

# ფუნქციის გამოძახება და შედეგის დაბეჭდვა
result = manual_find(main_string, str_to_find)
print(f"The index is: {result}")
