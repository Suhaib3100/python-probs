# Read the two input strings
string1 = input("Enter the first string: ").strip()
string2 = input("Enter the second string: ").strip()

# Normalize the strings: convert to lowercase and remove spaces
string1 = string1.lower().replace(" ", "")
string2 = string2.lower().replace(" ", "")

# Check if sorted characters of both strings are the same
if sorted(string1) == sorted(string2):
    print(True)  # The strings are anagrams
else:
    print(False)  # The strings are not anagrams