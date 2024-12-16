num = list(map(int,input().split()))
target = int(input())
pairs = []
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i] + num[j] == target:
            pairs.append(num[i],num[j])
print(pairs)
