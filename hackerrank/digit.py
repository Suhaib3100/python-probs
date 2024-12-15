t = int(input())
for _ in range(t):
    n= input().strip()
    num = int(n)
    divCount =0
    for digit in n:
        if digit != '0':
            if num % int(digit) == 0:
                divCount +=1
    print(divCount)