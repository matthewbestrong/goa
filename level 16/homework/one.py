# დააყენეთ სწორი მომხმარებლის სახელი და პაროლი
correct_username = "mate123"
correct_password = "12345"

# მომხმარებლის შეყვანის ინიციალიზაცია
username = ""
password = ""

# დაარეგულირეთ მანამ, სანამ მომხმარებლის სახელი და პაროლი სწორი იქნება
while username != correct_username or password != correct_password:
    username = input("Enter username: ")  # მომხმარებლის სახელის მოთხოვნა
    password = input("Enter password: ")  # მოითხოვეთ პაროლი

    # შეამოწმეთ, არის თუ არა რწმუნებათა სიგელები არასწორი
    if username != correct_username or password != correct_password:
        print("Invalid username or password. Try again.")

# წარმატებული შეტყობინების ამობეჭდვა
print("Access granted!")
