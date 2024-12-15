# Read input values
s, t = map(int, input().split())  # Start and end points of the house
a, b = map(int, input().split())  # Location of the apple and orange trees
m, n = map(int, input().split())  # Number of apples and oranges

# Read distances for apples and oranges
apples_distances = list(map(int, input().split()))
oranges_distances = list(map(int, input().split()))

# Initialize counters
count_apples = 0
count_oranges = 0

# Count apples that fall on the house
for d in apples_distances:
    if s <= a + d <= t:  # Check if the apple falls within the house range
        count_apples += 1

# Count oranges that fall on the house
for d in oranges_distances:
    if s <= b + d <= t:  # Check if the orange falls within the house range
        count_oranges += 1

# Print the results
print(count_apples)
print(count_oranges)