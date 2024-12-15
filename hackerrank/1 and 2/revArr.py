n= int(input())
arr = list(map(int,input().split()))
revArr = []
for i in range(n-1,-1,-1):
    revArr.append(arr[i])
print(" ".join(map(str,revArr)))