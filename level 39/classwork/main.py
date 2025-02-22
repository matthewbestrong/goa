# 1. Function that returns 'Hello World!'
def greet():
    return "Hello World!"  # უბრალოდ აბრუნებს სტრიქონს "Hello World!"

# 2. Count the number of sheep (True values) in a list
def count_sheeps(sheep):
    return sheep.count(True)  # ითვლის True-ების რაოდენობას სიაში

# 3. Remove all spaces from a given string
def no_space(x):
    return x.replace(" ", "")  # ცვლის ყველა space-ს ცარიელი სტრიქონით

# 4. Simple multiplication function
def double_integer(i):
    return i * 2  # რიცხვს ამრავლებს 2-ზე

# 5. Convert a name into a simple greeting
def greet(name):
    return f"Hello, {name} how are you doing today?"  # აბრუნებს მისალმებას სახელით

# 6. Return the opposite of a number
def opposite(number):
    return -number  # აბრუნებს რიცხვის საწინააღმდეგო მნიშვნელობას

# 7. Basic mathematical operation
def basic_op(operator, value1, value2):
    return eval(f"{value1}{operator}{value2}")  # ასრულებს არითმეტიკულ ოპერაციას

# 8. Convert time (hours) into seconds
def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000  # აბრუნებს დროის რაოდენობას მილიწამებში

# 9. Grow an array by multiplying all elements together
def grow(arr):
    result = 1
    for num in arr:
        result *= num  # ყველა ელემენტს ამრავლებს
    return result

# 10. Find the difference between two points
def distance_between_points(a, b):
    return ((b.x - a.x) ** 2 + (b.y - a.y) ** 2) ** 0.5  # ევკლიდეს მანძილის ფორმულა

# 11. Double each value in an array
def maps(a):
    return [x * 2 for x in a]  # თითოეულ ელემენტს ამრავლებს 2-ზე

# 12. Check if a hero has enough bullets to defeat dragons
def hero(bullets, dragons):
    return bullets >= dragons * 2  # ამოწმებს, აქვს თუ არა საკმარისი ტყვია დრაკონების მოსაკლავად

# 13. Sum an array of numbers
def sum_array(a):
    return sum(a)  # აბრუნებს სიაში არსებული რიცხვების ჯამს
