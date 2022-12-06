#!/usr/bin/env python3
for l in open("day06.in").readlines():
  solve = lambda l,n: next(i+n for i in range(0, len(l)) if len(set(l[i:i+n])) == n)
  print("Part 1:", solve(l, 4))
  print("Part 2:", solve(l, 14))
