# Creating a set with at least five elements
my_set = {10, 20, 30, 40, 50}

# Adding a new element to the set
my_set.add(60)

# Removing an existing element from the set
my_set.remove(30)  # If the element is not present, this will raise a KeyError

# Checking if a specific value is present in the set
is_present = 40 in my_set

# Printing the results
print("Updated Set:", my_set)
print("Is 40 present in the set?", is_present)
