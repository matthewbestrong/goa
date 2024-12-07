# სთხოვეთ მომხმარებელს შეიყვანოს ნომერი
number = float(input("Enter a number: "))

# შეამოწმეთ რიცხვი დადებითია, უარყოფითი თუ ნულოვანი
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print("The number is zero.")
