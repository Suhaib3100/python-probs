tc =int(input())
for _ in range(tc):
    n= int(input())
    arr = list(map(int,input().strip().split()))
    result = "NO"
    lsum = 0
    total = sum(arr)

    for i in range(0,len(arr)):
        rsum =total -arr[i] -lsum
        if lsum == rsum:
            result = "YES"
            break
        lsum += arr[i]
    print(result)
