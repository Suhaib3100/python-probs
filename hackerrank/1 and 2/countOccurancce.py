n = int(input())
numbers = list(map(int, input().split()))
unique_elements = []
occurrences = {}
for num in numbers:
 if num not in occurrences:
 occurrences[num] = 1
 unique_elements.append(num) # Keep track of the first
appearance order
 else:
 occurrences[num] += 1
for num in unique_elements:
 print(num, occurrences[num])
