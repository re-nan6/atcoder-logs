N = int(input())

Lflag = False
Rflag = False
nowL = 0
nowR = 0
tired_point = 0
for i in range(N):
  A,S = map(str,input().split())
  A = int(A)
  if S == "L":
    if not Lflag:
      Lflag = True
      nowL = A
    else:
      tired_point += abs(nowL-A)
      nowL = A
  else:
    if not Rflag:
      Rflag = True
      nowR = A
    else:
      tired_point += abs(nowR-A)
      nowR = A

print(tired_point)