tc = int(input())
for _ in range(tc):
    cA,cB,mc = map(int,input().split())
    distA = abs(cA - mc)
    disB = abs(cB -mc)
    if distA < disB:
        print("Cat A")
    elif disB < distA:
        print("Cat B")
    else:
        print("Mouse C")