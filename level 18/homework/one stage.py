correct_password = "Goa best"  # სწორი პაროლი
attempts = 0  # მრიცხველი არასწორი მცდელობისთვის

while True:
    password = input("Enter the password: ")  # Prompt the user
    if password == correct_password:
        print("Access granted!")
        break  # გამოდით ციკლიდან, როდესაც პაროლი სწორია
    else:
        attempts += 1  # გაზარდეთ მრიცხველი არასწორი მცდელობისთვის
        print("Incorrect password. Try again.")

print(f"Number of incorrect attempts: {attempts}")
