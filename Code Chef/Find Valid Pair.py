# cook your dish here
n = int(input())
lst = []

for i in range(n):
    a, b = map(int, input().split())
    lst.append([a,b])
    
    
# print(lst)

left, right = map(int, input().split())

for i in range(n):
    if left <=( lst[i][0] + lst[i][1] )<= right:
        if left <=( lst[i][0] * lst[i][1] )<= right:
            print(lst[i][0], lst[i][1])
            
