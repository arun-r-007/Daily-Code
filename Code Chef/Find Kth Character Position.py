# cook your dish here
s, c, k = input().split()

k = int(k)

count = 0

for i in range(len(s)):
    if s[i] == c:
        count += 1

        if count == k:
            print(i)
            break
else:
    print(-1)
    