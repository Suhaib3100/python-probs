n=int(input())
arr = list(map(int,input().split()))
evenSum = 0
oddSUm =0
for i in arr:
    if i%2 ==0:
        evenSum+=i
    else:
        oddSUm+=i
print(evenSum,end=" ")
print(oddSUm)