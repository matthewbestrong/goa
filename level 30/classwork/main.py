# მომხმარებლის სახელის შეტანა
name = input("Enter your name: ")

# არჩევანის შეტანა ("u" ან "l")
choice = input("Enter your choice ('u' for uppercase, 'l' for lowercase): ")

# პირობების მიხედვით შესაბამისი მოქმედება
if choice == "u":
    print(f"Your name in uppercase: {name.upper()}")
elif choice == "l":
    print(f"Your name in lowercase: {name.lower()}")
else:
    print("Wrong information.")
