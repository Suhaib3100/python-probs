t = int(input())  # Read the number of test cases
for _ in range(t):  # Loop through each test case
    m = int(input())  # Total money available
    n = int(input())  # Number of flavors
    cost = list(map(int, input().split()))  # List of flavor prices

    c = {}  # Initialize a dictionary for storing prices and their indices

    for i, price in enumerate(cost):  # Loop over flavors with index
        a = m - price  # Calculate the required complementary price
        
        if a in c:  # Check if the complementary price exists in the dictionary
            # If found, output its index plus one (1-based) and the current index
            print(c[a] + 1, i + 1)
            break  # Exit after finding the first valid pair
        
        c[price] = i  # Store the price with its index