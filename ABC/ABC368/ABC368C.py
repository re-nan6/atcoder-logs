N = int(input())
H = list(map(int,input().split()))
T = 0
for i in range(N):
  num = H[i] // 5
  T += num*3
  H[i] -= num*5
  while H[i] > 0:
    T += 1
    if T % 3 == 0:
      H[i] -= 3
    else:
      H[i] -= 1

print(T)