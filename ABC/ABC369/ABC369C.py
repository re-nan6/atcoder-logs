N = int(input())
A = list(map(int,input().split()))
ans = 0
if N == 1:
  print(1)
  exit()
now_diff = A[0] - A[1]
cnt = 2
cnt_diff = 0
for i in range(1,N-1):
  if A[i] - A[i+1] == now_diff:
    cnt += 1
  else:
    now_diff = A[i] - A[i+1]
    ans += 0.5*cnt*(cnt+1)
    cnt = 2
    cnt_diff += 1
ans += 0.5*cnt*(cnt+1)
print(int(ans)-cnt_diff)