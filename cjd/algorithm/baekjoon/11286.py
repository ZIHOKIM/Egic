import heapq
import sys
input = sys.stdin.readline # 빠른 입출력
hq = []
for _ in range(int(input())):
    n = int(input())
    if n != 0:
        heapq.heappush(hq,(abs(n),n))
    else:
        if len(hq) != 0:
            print(heapq.heappop(hq)[1])
        else:
            print(0)

# 강의 코드
# pq = []
# for _ in range(int(input())):
#     x = int(input())
#     if x:
#       heapq.heappush(pq,(abs(x),x))
#     else:
#       print(heapq.heappop(pq) if pq else 0)


