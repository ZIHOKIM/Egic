from collections import deque
dq = deque(list(range(1,int(input())+1)))

while len(dq)!=1:
    dq.popleft()
    dq.append(dq.popleft())

print(*dq)


# 강의 코드
# N = int(input())
# dq = deque(range(1,N+1))
#
# while len(dq) > 1:
#     dq.popleft()
#     dq.append(dq.popleft())
# print(dq.popleft())
