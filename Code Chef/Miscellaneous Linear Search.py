# cook your dish here

n = int(input())

pairs = []

for i in range(n):
    a, b = map(int, input().split())
    pairs.append([a, b])

x, y = map(int, input().split())

flag = "No"

for a, b in pairs:
    if (a == x and b == y) or (a == y and b == x):
        flag = "Yes"
        break

print(flag)
