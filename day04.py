#!/usr/bin/env python3
part1, part2 = 0, 0
for l in open("day04.in").readlines():
  p = [[int(y) for y in x.split("-")] for x in l.split(",")]
  part1 += p[0][0] <= p[1][0] and p[0][1] >= p[1][1] or p[0][0] >= p[1][0] and p[0][1] <= p[1][1]
  p.sort()
  part2 += p[0][1] >= p[1][0]
print(part1, part2)
