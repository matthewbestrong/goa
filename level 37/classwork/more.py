# ფუნქციის შექმნა, რომელიც შლის დუპლიკატებს
def no_duplicates(user_list):
    return list(set(user_list))  # სიის გარდაქმნა set-ად, შემდეგ ისევ list-ად

# ფუნქციის გამოძახება სხვადასხვა არგუმენტებით
list1 = [1, 2, 2, 3, 4, 4, 5]
list2 = ["apple", "banana", "apple", "cherry", "banana"]
list3 = [10, 20, 30, 10, 40, 50, 30]

# შედეგების დაბეჭდვა
print("Original:", list1, "-> Without Duplicates:", no_duplicates(list1))
print("Original:", list2, "-> Without Duplicates:", no_duplicates(list2))
print("Original:", list3, "-> Without Duplicates:", no_duplicates(list3))
