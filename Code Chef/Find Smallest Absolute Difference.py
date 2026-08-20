# cook your dish here
n, k = map(int, input().split())
arr = list(map(int, input().split()))

min_diff = float('inf')
result = None

for i in range(n):
    diff = abs(arr[i] - k)

    if diff < min_diff:
        min_diff = diff
        result = arr[i]
    elif diff == min_diff:
        result = min(result, arr[i])

print(result)