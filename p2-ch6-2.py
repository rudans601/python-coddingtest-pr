n = int(input())
l = []
for i in range(n):
    a,b = input().split()
    l.append((a,int(b)))

l = sorted(l, key=lambda l: l[1])

for student in l:
    print(student[0],end=" ")