sentence = input()
vowels = "aeiouAEIOU"
res = ""
for i in sentence:
    if i in vowels:
        res+="_"
    else:
        res+=i
print(res)