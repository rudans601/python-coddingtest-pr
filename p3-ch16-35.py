# n = int(input())

# data = [0,0,0]
# ugly = [1]
# for i in range(1,n):
#     for j in range(3):
#         data[j] += 1
#         answer = 0
#         for k in range(3):
#             if k == 0:
#                 answer += data[k] * 2
#             elif k == 1:
#                 answer += data[k] * 3
#             elif k == 2:
#                 answer += data[k] * 5
#         ugly.append(answer)

# ugly.sort()
# print(ugly[n-1])

n = int(input())

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0
next2, next3,next5 = 2,3,5

for l in range(1,n):
    ugly[l] = min(next2,next3,next5)
    
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5+= 1
        next5 = ugly[i5] * 5
        
print(ugly[n-1])