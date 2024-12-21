# სიის შექმნა 10 ელემენტით
my_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# მომხმარებლისგან ორი მთელი რიცხვის მიღება
num1 = int(input("Enter the first number (num1): "))
num2 = int(input("Enter the second number (num2): "))

# შემოწმება num1 და num2-ს შორის ურთიერთობის მიხედვით
if num1 > num2:
    # slicing num1-დან num2-მდე
    new_list = my_list[num2:num1]
    print("New sliced list:", new_list)
elif num2 > num1:
    # slicing num2-დან num1-მდე
    new_list = my_list[num1:num2]
    print("New sliced list:", new_list)
else:
    # თუ num1 და num2 ტოლია
    print("New sliced list: []")
