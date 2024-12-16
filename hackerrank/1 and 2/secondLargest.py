# Read input: a space-separated string of integers
num = list(map(int, input("Enter the numbers separated by spaces: ").split()))

# Remove duplicates and sort the numbers
sortedSet = sorted(set(num))

# Get the second largest number if possible
secondLarge = sortedSet[-2] if len(sortedSet) >= 2 else None

# Output the result
if secondLarge is not None:
    print("The second largest number is:", secondLarge)
else:
    print("There is no second largest number.")