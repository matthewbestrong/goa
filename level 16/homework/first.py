# დააყენეთ სწორი პაროლი
correct_password = "my_secret"

# მომხმარებლის შეყვანის ინიციალიზაცია
user_input = ""

# გააგრძელეთ მომხმარებლის მოთხოვნა, სანამ სწორი პაროლი არ შეიყვანება
while user_input != correct_password:
    user_input = input("Enter the password: ")  # შესთავაზეთ მომხმარებელს
    if user_input != correct_password:
        print("Incorrect password. Try again.")

# წარმატებული შეტყობინების ამობეჭდვა
print("Access granted!")
