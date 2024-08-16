# Identify named constant
TAX_RATE = 0.0065

# Get lot number from user
lot_number = int(input("Enter the lot number or 0 to terminate: "))

 # Iterate while lot number is not 0
while lot_number != 0:

  # Get property value
  property_value = float(input(f"What is lot {lot_number}'s value? "))

  # Calculate tax
  property_tax = property_value * TAX_RATE

  # Display tax
  print(f"Property tax for lot {lot_number} is ${property_tax:.2f}.")

  # Get next lot number
  lot_number = int(input("Enter the next lot number or 0 to terminate: "))