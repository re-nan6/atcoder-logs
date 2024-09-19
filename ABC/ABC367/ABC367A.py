A,B,C = map(int,input().split())
time = B

while time != C:
  if time == A:
    print("No")
    exit()
  time += 1
  time %= 24

print("Yes")