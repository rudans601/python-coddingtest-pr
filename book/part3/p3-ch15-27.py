from bisect import bisect_left, bisect_right

n,x = map(int,input().split())
data = list(map(int,input().split()))

def cal_range(data, left_value, right_value):
    r_i = bisect_right(data, right_value)
    l_i = bisect_left(data, left_value)
    return r_i - l_i if r_i - l_i != 0 else -1

print(cal_range(data,x,x))
# 정답 맞춤
# 정답 코드(직접 구현)

def count_by_value(array,x):
    n = len(array)
    a = first(array,x,0,n-1)
    if a == None:
        return 0
    b = last(array,x,0,n-1)
    return b - a + 1

def first(array,target,start,end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array,target,start,mid-1)
    else:
        return first(array,target,mid+1,end)
    
def last(array,target,start,end):
    if start > end:
        return None
    mid = (start+end) // 2
    if (mid == n-1 or target < array[mid+1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array,target,start,mid-1)
    else:
        return last(array, target, mid+1,end)

n,x = map(int,input().split())
array = list(map(int,input().split()))

count = count_by_value(array,x)

if count == 0:
    print(-1)
else:
    print(count)