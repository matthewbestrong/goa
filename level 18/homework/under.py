# დაარეგულირეთ 5-ჯერ მომხმარებლის შეყვანის მისაღებად
for i in range(5):
    # სთხოვეთ მომხმარებელს შეიყვანოს ნომერი
    number = int(input(f"Enter number {i + 1}: "))
    
    # შეამოწმეთ რიცხვი ლუწია თუ კენტი
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
