# ორი ბულეანი და ლოგიკური ოპერატორები
print(True and False)      # False
print(True or False)       # True

# სამი ბულეანი და ლოგიკური ოპერატორები
print(True and True and False)    # False
print(False or True or False)     # True
print(True and (False or True))   # True
print((True or False) and False)  # False



# ცვლადების განსაზღვრა
a = 25
b = 35
c = 40
d = 50

# 1. a არის 20-ზე მეტი და b არის 30-ზე ნაკლები
print(a > 20 and b < 30)  # False

# 2. c არის 35-ზე მეტი ან d არის 45-ზე მეტი
print(c > 35 or d > 45)  # True

# 3. a არის 20-ზე მეტი და c ნაკლებია d-ზე
print(a > 20 and c < d)  # True

# 4. b არის 40-ზე ნაკლები და a არის 30-ზე ნაკლები
print(b < 40 and a < 30)  # True

# 5. d არის 50 და c ნაკლებია 100-ზე
print(d == 50 and c < 100)  # True

# 6. a ნაკლებია b-ზე და d მეტია 40-ზე
print(a < b and d > 40)  # True

# 7. c არის 35-ზე მეტი ან a ნაკლებია 10-ზე
print(c > 35 or a < 10)  # True

# 8. b ტოლია 35-ის და d მეტია 45-ზე
print(b == 35 and d > 45)  # True

# 9. a ნაკლებია 30-ზე ან b ნაკლებია 40-ზე და c მეტია 25-ზე
print((a < 30 or b < 40) and c > 25)  # True

# 10. d არის 50 და a არ არის ტოლი 25-ის
print(d == 50 and a != 25)  # False


















