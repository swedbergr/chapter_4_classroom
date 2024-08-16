# Loop through block of code for each new salesman
for salesman in ["Jim", "Dwight", "Stanley", "Phillys", "Andy"]:
  # Get salesman's infomration
  sales = float(input(f"Enter the amount of sales for {salesman}: "))
  comm_rate = float(input(f"Enter the commission rate for {salesman}: "))

  # Calculate the commission
  commission = sales * comm_rate

  # Display commission
  print(f"{salesman}'s commission is ${commission:.2f}.")