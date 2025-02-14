# Creating a list with duplicate elements
my_list = [10, 20, 30, 20, 40, 30, 50, 10]

# Converting the list to a set to remove duplicates
unique_set = set(my_list)

# Converting the set back to a list
unique_list = list(unique_set)

# Printing the results
print("Original List:", my_list)
print("List after Removing Duplicates:", unique_list)
