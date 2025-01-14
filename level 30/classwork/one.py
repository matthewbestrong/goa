def manual_swapcase(input_str):
    # ცარიელი შედეგის სტრინგი
    swapped_str = ""
    
    # სტრინგზე ციკლის გაშვება
    for char in input_str:
        # თუ სიმბოლო არის პატარა, გადავაქციოთ დიდად
        if char.islower():
            swapped_str += char.upper()
        # თუ სიმბოლო არის დიდი, გადავაქციოთ პატარად
        elif char.isupper():
            swapped_str += char.lower()
        # თუ სიმბოლო არ არის ასო, დავამატოთ პირდაპირ
        else:
            swapped_str += char
    
    return swapped_str

# მაგალითი
test_string = input("Enter a string: ")
print("Swapped case string:", manual_swapcase(test_string))
