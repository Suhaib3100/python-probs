sentence = input()
cleaned = ""
for char in sentence:
    if char.isalnum():
        cleaned+=char.lower()
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not")
