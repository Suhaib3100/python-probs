num = list(map(int,input().split()))
uniqueNum = []
for i in num:
    if i not in uniqueNum:
        uniqueNum.append(num)
print(uniqueNum)