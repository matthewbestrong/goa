# აიღეთ ორი რიცხვი შეყვანად
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# მიიღეთ ოპერატორი შეყვანის სახით
operator = input("Enter an operator (+, -, *, /): ")

# შეასრულეთ გაანგარიშება ოპერატორის საფუძველზე
if operator == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")
elif operator == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")
elif operator == "/":
    if num2 != 0:  # შეამოწმეთ ნულზე გაყოფის თავიდან ასაცილებლად
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")

# პროგრამის დასასრული
print("Calculation complete.")
