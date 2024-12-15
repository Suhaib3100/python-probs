list1= list(map(int,input().split()))
list2 = list(map(int,input().split()))
common = []
for element in list1:
    if element in list2 and element not in common:
        common.append(element)
print(" ".join(map(str,common)))