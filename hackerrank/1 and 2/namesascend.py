n = int(input())
names = []
for _ in range(n):
 names.append(input())
names.sort()
for name in names:
 print(name)