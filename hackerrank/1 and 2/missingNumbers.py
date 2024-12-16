# Read the number of elements
n = int(input())

# Read the space-separated integers and store them in a list
num = list(map(int, input().split()))

# Convert the input list to a set for efficient look-up
num_set = set(num)

# Initialize an empty list to store missing numbers
missing = []

# Find the missing numbers from 1 to n
for i in range(1, n + 1):
    if i not in num_set:  # Check using set for efficiency
        missing.append(i)

# Output results
if missing:
    print(" ".join(map(str, missing)))  # Print missing numbers
else:
    print("NA")  # Print "NA" if no numbers are missing