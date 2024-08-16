# Get range of divisors from user
min = int(input("Enter the smallest number in the divisor range: "))
max = int(input("Enter the largest number in the divisor range: "))

# Validate that the min is smaller than the max
while max <= min:
  print("ERROR! The smallest number should be smaller than the larger number.")
  min = int(input("Enter the smallest number in the divisor range: "))
  max = int(input("Enter the largest number in the divisor range: "))

# Iterate for every number in the range
for divisor in range(min,max + 1):
  if divisor == 0:
    print("UND ", end="")
    continue
  inverse = 1 / divisor
  print(inverse, end=" ")