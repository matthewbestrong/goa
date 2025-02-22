# 10. Find the difference between two points
def distance_between_points(a, b):
    return ((b.x - a.x) ** 2 + (b.y - a.y) ** 2) ** 0.5  # ევკლიდეს მანძილის ფორმულა
