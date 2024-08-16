# Get number of grades from ther user
number_of_grades = int(input("How many grades need averaged? "))

# Set accumulator
sum = 0

# Iterate for each grade to prompt the user for each grade and add to accumulator
for assignment in range(number_of_grades):
  grade = float(input("Grade: "))
  sum += grade

# Calculate the average
average = sum / number_of_grades

# Display average
print(f"The average of the {number_of_grades} assignment is {average}%.")