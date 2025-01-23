from bisect import bisect_left, bisect_right

n = int(input())
data = list(map(int,input().split()))
answer = False
for i in data:
    if bisect_left(data,i) == i:
        print(i)
        answer = True
if not answer:
    print(-1)
#정답 맞춤
#정답 코드

def binary_search(array,start,end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array,start,mid-1)
    else:
        return binary_search(array,mid+1,end)

n = int(input())
array = list(map(int,input().split()))

index = binary_search(array,0,n-1)

if index == None:
    print(-1)
else:
    print(index)