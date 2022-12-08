#!/usr/bin/env python3
f = open("day08.in").readlines()
v = [[False for x in y.strip()] for y in f]
l = len(f)
for i in range(0, l):
  m = ['/'] * 4
  for j in range(0, l):
    for x, (a, b) in enumerate(((i, j), (i, l-j-1), (j, i), (l-j-1, i))):
      if f[a][b] > m[x]:
        v[a][b] = True
        m[x] = f[a][b]
print("Part 1:", sum([sum(x) for x in v]))

highest = 0
def view(r, x):
  result = 0
  for k in r:
    result += 1
    if x(f, k) >= value:
      break
  return result
for i in range(0, l):
  for j in range(0, l):
    value = f[i][j]
    highest = max(highest,
      view(range(i+1, l), lambda f, k: f[k][j]) *
      view(range(i-1, -1, -1), lambda f, k: f[k][j]) *
      view(range(j+1, l), lambda f, k: f[i][k]) *
      view(range(j-1, -1, -1), lambda f, k: f[i][k]))
print("Part 2:", highest)
