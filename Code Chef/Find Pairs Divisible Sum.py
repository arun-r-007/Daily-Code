# cook your dish here
n, k = map(int, input().split())
result = ()

for i in range(n):
    a, b = map(int, input().split())
    if (a+b)%k == 0:
        result = result + ((a,b),)
    
for pair in result:
    print(pair)