N = int(input())
genso_list = []
for i in range(N):
  A = list(map(int,input().split()))
  genso_list.append(A)

now_genso = 1
for j in range(1,N+1):
  if now_genso >= j:
    now_genso = genso_list[now_genso-1][j-1]
  else:
    now_genso = genso_list[j-1][now_genso-1]

print(now_genso)