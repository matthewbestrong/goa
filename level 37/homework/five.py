# Creating two sets with some common elements
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Performing union operation (combines all unique elements from both sets)
union_set = set1.union(set2)  # or set1 | set2

# Performing intersection operation (finds common elements)
intersection_set = set1.intersection(set2)  # or set1 & set2

# Performing difference operation (elements in set1 but not in set2)
difference_set = set1.difference(set2)  # or set1 - set2

# Printing the results
print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (Set1 - Set2):", difference_set)
