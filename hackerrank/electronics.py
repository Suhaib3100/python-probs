budget,nk,nu = map(int,input().split())
keyPrice = list(map(int,input().split()))
usbPrice = list(map(int,input().split()))
result = -1
keyPrice.sort(reverse=True)
usbPrice.sort()
i,j  = 0,0
while i<len(keyPrice) and j<len(usbPrice):
    cost = keyPrice[i] + usbPrice[j]
    if cost<=budget:
        result = max(cost,result)
        j+=1
    else:
        i+=1
if result != -1:
    print(result)
else:
    print(-1)