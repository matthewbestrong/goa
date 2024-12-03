# ცვლადის ინიცირება 0-მდე
number = 0

# გამოიყენეთ while ციკლი ლუწი რიცხვების დასაბეჭდად
while number <= 20:
    print(number)
    number += 2  # გაზარდეთ 2-ით შემდეგი ლუწი რიცხვის მისაღებად






    # ცვლადის ინიციალიზაცია 1-მდე (პირველი კენტი რიცხვი)
number = 1

# გამოიყენეთ while ციკლი კენტი რიცხვების დასაბეჭდად
while number <= 20:
    print(number)
    number += 2  # გაზარდეთ 2-ით შემდეგი კენტი რიცხვის მისაღებად









    # გადახედეთ რიცხვებს 10-დან 30-მდე
for number in range(10, 31):
    # შეამოწმეთ რიცხვი ლუწია თუ კენტი და დაბეჭდეთ შედეგი
    if number % 2 == 0:
        print(f"{number} - even")
    else:
        print(f"{number} - odd")






# სთხოვეთ მომხმარებელს შეიყვანოს ორი ნომერი
num1 = int(input("Enter the first number (num1): "))
num2 = int(input("Enter the second number (num2): "))

if num1 > num2:
    # პირველი რიცხვი უფრო დიდია: დაბეჭდეთ ლუწი რიცხვები num2-დან num1-მდე (მათ შორის)
    print(f"Even numbers from {num2} to {num1}:")
    for number in range(num2, num1 + 1):
        if number % 2 == 0:
            print(number, end=" ")
else:
    # მეორე რიცხვი უფრო დიდია: ამობეჭდეთ კენტი რიცხვები num1-დან num2-მდე (მათ შორის)
    print(f"Odd numbers from {num1} to {num2}:")
    for number in range(num1, num2 + 1):
        if number % 2 != 0:
            print(number, end=" ")

# დაასრულეთ გამომავალი ახალი ხაზით უკეთესი ფორმატირებისთვის
print()











