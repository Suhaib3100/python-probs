n, d = map(int, input().split())
arr = list(map(int, input().split()))

# Calculate effective rotations
d = d % n  # In case d >= n, we only need to rotate d % n times

# Perform the rotation using slicing
result = arr[d:] + arr[:d]
print(" ".join(map(str, result)))