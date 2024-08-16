# Get number of steps from user
steps = int(input("Enter the number of steps: "))

# Iterate for rows
for r in range(steps):
  # Iterate for columns
  for c in range(r + 1):
    # Print #
    print("#", end="")

  # Go to next row
  print("")