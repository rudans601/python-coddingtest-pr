n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
    
result = sorted(l,reverse=True)

for i in result:
    print(i,end=" ")