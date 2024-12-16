inputStr = input()
charCount = {}
for char in inputStr:
    if char in charCount:
        charCount[char] +=1
    else:
        charCount[char] =1
for char in inputStr:
    if charCount[char] ==1:
        print(char)
    else:
        print(-1)