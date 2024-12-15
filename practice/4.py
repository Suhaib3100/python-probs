# Read input values
s, t = map(int, input().split())  # Start and end of Sam's house
a, b = map(int, input().split())  # Positions of the apple and orange trees
m, n = map(int, input().split())  # Number of apples and oranges
appDist = list(map(int, input().split()))  # Distances apples fall
orangeDist = list(map(int, input().split()))  # Distances oranges fall

appCount = 0  # Counter for apples
oraCount = 0  # Counter for oranges

# Calculate the positions of apples
for d in appDist:
    if s <= (a + d) <= t:  # Check if the apple falls within the bounds of the house
        appCount += 1  # Increment apple count

# Calculate the positions of oranges
for d in orangeDist:
    if s <= (b + d) <= t:  # Check if the orange falls within the bounds of the house
        oraCount += 1  # Increment orange count

# Print the results
print(appCount)  # Number of apples on the house
print(oraCount)  # Number of oranges on the house