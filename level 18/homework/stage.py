# სთხოვეთ მომხმარებელს შეიყვანოს ნომერი
number = int(input("Enter a number: "))

# შეამოწმეთ, იყო თუ არა რიცხვი 5-ზე
if number % 5 == 0:
    print(f"{number} is divisible by 5.")
else:
    print(f"{number} is not divisible by 5.")
