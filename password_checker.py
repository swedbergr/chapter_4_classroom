# Store password for comparison
password = "whippets"

# Prompt for priming input
pass_check = input("Enter the password: ")

# Initialize counter
counter = 0

# Loop for incorrect password attempts
while pass_check != password:
  # Increment counter
  counter += 1

  # Lock out if counter reaches 4
  if counter >= 4: break

  # Display error and reprompt
  print("Woopsidoodle, that looks like the incorrect password. Please try again.")
  pass_check = input("Please enter the correct password: ")

# Main protected program
else:
  print("This is a protected part of the program.")

# Display locked out message
if counter >= 4: print("You have been locked out.")