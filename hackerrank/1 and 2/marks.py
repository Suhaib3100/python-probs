n= int(input())
arr = list(map(int,input().split()))
limit1 = int(input())
limit2 = int(input())
count =0
totalSum =0
for i in arr:
    if limit1 < i < limit2:
        totalSum +=i
        count +=1
if count> 0:
    average = totalSum / count
    print(int(average))
else:
    print(0)
