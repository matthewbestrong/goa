# 5. Convert a full name to initials
def abbrev_name(name):
    return ".".join([word[0].upper() for word in name.split()])  # აბრუნებს ინიციალებს დიდი ასოებით
