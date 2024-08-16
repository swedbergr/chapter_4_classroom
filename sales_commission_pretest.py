# Prompt the user to initially set the loop condition
new_salesman = input("Are you ready to enter the first salesman? Type Y for yes and N for no. ")

# Loop through block of code for each new salesman
while new_salesman == "Y":
  # Get salesman's infomration
  name = input("Enter the salesman's name: ")
  sales = float(input(f"Enter the amount of sales for {name}: "))
  comm_rate = float(input(f"Enter the commission rate for {name}: "))

  # Calculate the commission
  commission = sales * comm_rate

  # Display commission
  print(f"{name}'s commission is ${commission:.2f}.")

  # Prompt for another salesman
  new_salesman = input("Do you have another salesman? Type Y for yes and N for no. ")