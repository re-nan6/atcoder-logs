S = input()
T = input()

tmp = []
ans = []

for i in range(len(S)):
  if S[i] > T[i]:
    tmp.append(i)

for i in range(len(S)-1,-1,-1):
  if S[i] < T[i]:
    tmp.append(i)

size = len(tmp)
for i in range(size):
  tmpS = list(S)
  tmpS[tmp[i]] = T[tmp[i]]
  S = ''.join(tmpS)
  ans.append(S)

print(size)
for i in range(size):
  print(ans[i])