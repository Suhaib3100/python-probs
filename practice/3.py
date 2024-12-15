budget,nk,nu = map(int,input().split())
keyCost = list(map(int,input().split()))
usbCost = list(map(int,input().split()))
result =-1
i,j= 0,0
while(i<keyCost and j<usbCost):
    cost = keyCost[i] + usbCost[j]
    if cost <=budget:
        result = max(cost,result)
        j+=1
    else:
        i+=1
print(result)