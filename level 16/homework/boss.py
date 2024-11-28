# სთხოვეთ მომხმარებელს ნომერი
number = int(input("Enter a number to find its factors: "))

# გამყოფის ინიციალიზაცია
divisor = 1

print(f"Factors of {number} are:")

# გამოიყენეთ while loop ფაქტორების მოსაძებნად
while divisor <= number:
    if number % divisor == 0:  # შეამოწმეთ არის თუ არა გამყოფი ფაქტორი
        print(divisor)
    divisor += 1  # გამყოფის გაზრდა
