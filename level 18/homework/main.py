# მომხმარებლისთვის ორი რიცხვის შემოტანა
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# უდიდესის გამოთვლა და დაბეჭდვა
if num1 > num2:
    print(f"The largest number is: {num1}")
elif num2 > num1:
    print(f"The largest number is: {num2}")
else:
    print("Both numbers are equal.")
