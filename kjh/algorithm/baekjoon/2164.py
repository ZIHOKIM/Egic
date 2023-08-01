from collections import deque
num = int(input())
dq = deque()
for i in range(num):
    dq.append(i+1)

for j in range(num):
    dq.popleft()
    dq.append(dq.popleft())

print(dq)
if len(dq)==1:
    print(dq)
