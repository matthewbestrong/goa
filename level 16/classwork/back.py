import random

# ვქმნით my_num ცვლადს 1-დან 10-მდე შემთხვევითი რიცხვით
my_num = random.randint(1, 10)

# ინიციალიზაცია მცდელობების რაოდენობისთვის
attempts = 0

print("გამოიცანით 1-დან 10-მდე რიცხვი!")

while True:
    # მომხმარებლის შეყვანა
    user_guess = int(input("შეიყვანეთ თქვენი რიცხვი: "))
    attempts += 1  # მცდელობების გაზრდა

    # თუ მომხმარებლის შეყვანილი რიცხვი სწორია
    if user_guess == my_num:
        print("You guessed!")
        break
    else:
        print("Wrong guess, try again.")

# დაბეჭდეთ მცდელობების რაოდენობა
print(f"თქვენ {attempts} მცდელობა დაგჭირდათ.")
