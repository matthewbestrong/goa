# 9. Grow an array by multiplying all elements together
def grow(arr):
    result = 1
    for num in arr:
        result *= num  # ყველა ელემენტს ამრავლებს
    return result