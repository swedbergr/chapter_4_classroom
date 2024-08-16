# Get the number base from user
base = int(input("What the base you want to write out? "))

# Iterate for ten's place
for ten in range(base):
  # Iterate for one's place
  for one in range(base):
    # Display number
    print(f"{ten}{one}", end=" ")