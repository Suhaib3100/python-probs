sentence = input()
word = sentence.split()
initials = ""
for i in word:
    initials +=i[0]
print(initials)