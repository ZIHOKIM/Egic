n = int(input())

for _ in range(n):
    a = input()
    cnt = 0
    result = "YES"
    for i in a:
        if i=="(":
            cnt += 1
        elif i==")":
            cnt -= 1
        if cnt < 0:
            result = "NO"
            break
    if cnt != 0:
        result = "NO"
    print(result)

# 강의 코드
# for _ in range(int(input())):
#     stk = []
#     isVPS = True
#     for ch in input():
#         if ch == '(':
#             stk.append(ch)
#         else:
#             if stk:
#                 stk.pop()
#             else:
#                 isVPS = False
#     if len(stk) > 0:
#         isVPS = False
#
#     print('YES' if isVPS else 'NO')
