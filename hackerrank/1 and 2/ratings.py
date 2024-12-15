n=int(input())
num = list(map(int,input().split()))
large = num[0]
for i in range(1,n):
    if num[i] >large:
        large = num[i]
print(large)
