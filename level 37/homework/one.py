# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)

# Attempting to modify the second element
try:
    my_tuple[1] = 99  # Tuples are immutable, this should raise an error
except TypeError as e:
    print("Error:", e)
