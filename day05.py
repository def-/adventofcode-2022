#!/usr/bin/env python3
import re
p1, p2 = open("day05.in").read().split("\n\n")
s = [[], [], [], [], [], [], [], [], []]
for l in p1.splitlines()[::-1][1:]:
  for i in range(9):
    if l[i*4+1] != ' ':
      s[i].append(l[i*4+1])
for l in p2.splitlines():
  n, f, t = re.match(r"move (\d+) from (\d+) to (\d+)", l).groups()
  n, f, t = (int(n), int(f)-1, int(t)-1)
  # Part 1
  #for i in range(n):
  #  s[t].append(s[f].pop())
  # Part 2
  s[t].extend(s[f][-n:])
  del s[f][-n:]
print(''.join([x[-1] for x in s]))
