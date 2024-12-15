numbers = tuple(map(int,input().split()))
sum =0
prod =1
for i in numbers:
    sum += i
    prod *= i
print(sum,end=" ")
print(prod)