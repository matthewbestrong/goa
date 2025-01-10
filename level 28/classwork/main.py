def manual_index(main_string, search_string):
    # შეამოწმებს, არის თუ არა საძიებელი სთრინგი მთავარ სთრინგში
    if search_string in main_string:
        return main_string.index(search_string)  # დააბრუნებს საძიებელი სთრინგის ინდექსს
    else:
        return -1  # თუ საძიებელი სთრინგი ვერ მოიძებნა, დააბრუნებს -1

# ტესტირება:
main_string = "Hello, welcome to the world of Python"
search_string = "welcome"
print(manual_index(main_string, search_string))  # უნდა დააბრუნოს 7
