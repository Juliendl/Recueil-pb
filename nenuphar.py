w, h = [int(i) for in in input().split()]
x, y = [int(i) for in in input().split()]
n = input()

lake = {}
lake[x, y] = 1

for d in range(n):
  for (cx, cy) in list(lake.keys()):
    for dx, dy in (0,1),(0,-1),(-1,0),(1,0),(1,1),(-1,-1),(1,-1),(-1,1):
      nx, ny = cx+dx, cy+dy
      if 0<=nx<w and 0<=ny<h:
        lake[nx, ny] = 1

print(len(lake))
