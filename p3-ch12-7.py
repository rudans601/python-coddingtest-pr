n = input()
a = 0
b = 0
for i in range(len(n) // 2):
    a += int(n[i])

for j in range(len(n) // 2, len(n)):
    b += int(n[j])
    
print("LUCKY" if a == b else "READY")
