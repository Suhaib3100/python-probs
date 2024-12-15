a = int(input())
for _ in range(a):
    x,y,z = map(int,input().split())
    dista = abs(x-z)
    distb = abs(y-z)
    if dista < distb:
        print("Cat A")
    elif dista > distb:
        print("Cat B")
    else:
        print("Mouse C")
