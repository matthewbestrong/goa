# ცვლადების შექმნა input-ის გამოყენებით
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))  # ასაკი მთლიან რიცხვად გარდაქმნა
number1 = float(input("Enter the first number: "))  # რიცხვი ათწილადების სახით
number2 = float(input("Enter the second number: "))  # რიცხვი ათწილადების სახით

# თითოეული ცვლადის ტიპის დაბეჭდვა
print("The type of 'name' is:", type(name))
print("The type of 'surname' is:", type(surname))
print("The type of 'age' is:", type(age))
print("The type of 'number1' is:", type(number1))
print("The type of 'number2' is:", type(number2))
