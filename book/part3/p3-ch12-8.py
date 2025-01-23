s = input()
result = 0
q = []
for i in s:
    if 48 <= ord(i) and ord(i) <= 57:
        result += ord(i) - 48
    else:
        q.append(i)

q.sort()
print(q)
print(result)

# 실행이 안돼서 정답 확인
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
        
result.sort()

if value != 0:
    result.append(str(value))
    
print("".join(result))