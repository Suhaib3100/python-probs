# Read the number of bird sightings (though we won't necessarily need to use this variable)
t = int(input())
# Read the bird types from input as a list of integers
birdType = list(map(int, input().split()))

# Initialize a dictionary to count occurrences of each bird type
birdOccurance = {}

# Count the occurrences of each bird type
for i in birdType:
    if i in birdOccurance:
        birdOccurance[i] += 1  # Increment count if the bird type exists
    else:
        birdOccurance[i] = 1  # Initialize count if it's the first sighting

# Find the maximum frequency of sightings
frequency = max(birdOccurance.values())

# Initialize a list to hold bird types that have the maximum frequency
mostFreq = []
# Find all bird types that have the maximum frequency
for bird, count in birdOccurance.items():
    if count == frequency:
        mostFreq.append(bird)  # Add the bird type to the list

# Output the smallest bird type ID among those with maximum frequency
print(min(mostFreq))