# Get input from user for starting perfect square
start = int(input("The first number to be squared: "))

# Get input from user for last perfect square
last = int(input("The last number to be squared: "))

# Format display
print("Number\tSquare")
print("--------------")

# Iterate for each perfect square between user inputs
for num in range(start, last + 1):
  print(f"{num}\t{num ** 2}")