# Read the size of the staircase
n = int(input())

# Loop to build the staircase
for i in range(n):
    # Calculate the number of leading spaces and # symbols
    spaces = ' ' * (n - i - 1)   # Number of spaces
    hashes = '#' * (i + 1)        # Number of hashes
    
    # Print the staircase row
    print(spaces + hashes)