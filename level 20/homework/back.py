# Take two numbers as input
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Initialize the sum to 0
total_sum = 0

# Use a loop to calculate the sum between start and end
for num in range(start, end + 1):
    total_sum += num

# Print the result
print(f"The sum of numbers between {start} and {end} is: {total_sum}")
