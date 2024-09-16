N = int(input())
A = list(map(int,input().split()))

dp_even = [0]*(N)
dp_odd = [-float("inf")]*(N)
dp_odd[0] = A[0]
for i in range(1,N):
  dp_even[i] = max(dp_even[i-1],dp_odd[i-1]+2*A[i])
  dp_odd[i] = max(dp_odd[i-1],dp_even[i-1]+A[i])

print(max(dp_even[N-1],dp_odd[N-1]))