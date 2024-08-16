# Get number of steps from the user
steps = int(input("Number of stair steps:" ))

# Iterate for rows
for r in range(steps):
  # Iterate for columns
  for c in range(steps):
    # Check for equal target values
    if r == c:
      # Print #
      print("#", end="")
    else:
      # Print space
      print(" ", end="")

  # Go to next row
  print("")