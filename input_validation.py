# Define name constant
MARK_UP = 2.5
next = 'y'

# Process one or more items
while next == 'y':
  # Get the item's wholesale cost
  wholesale = float(input("Enter the item's wholesale cost: "))

  # Check wholesale for good data
  while wholesale < 0:
    # Error message
    print("The wholesale amount can not be negative. ")

    # Reprompt for wholesale
    wholesale = float(input("Enter the item's wholesale cost: "))

  # Calculate the retail price
  retail = wholesale * MARK_UP

  # Display the retail price
  print(f"Retail price: ${retail:.2f}")

  # Check for another item
  next = input("Is there another item? Type y for yes and n for no. ")