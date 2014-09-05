#-*- encoding: utf-8 -*-
"""
Number spiral diagonals

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

[21]  22 23  24 [25]
20  [ 7]  8 [ 9] 10
19    6 [ 1]  2  11
18  [ 5]  4 [ 3] 12
[17] 16  15  14 [13]

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

from utils import *

N = 1001

# version 1
M = Matrix(N, N)
pos = (N / 2, N / 2)
M[pos] = 1
pos = vadd(pos, (0, 1))
dire = 1
step = 1
circle = 3
turn = 0
for i in range(2, N * N + 1):
    M[pos] = i
    step += 1
    if step == circle:
        step = 1
        turn += 1
        if turn == 4:
            turn = 0
            circle += 2
            pos = vadd(pos, dire4[dire])
            dire = (dire + 1) % 4
            continue
        dire = (dire + 1) % 4
    pos = vadd(pos, dire4[dire])
print sum(M[i] for i in M.indexs() if i[0] == i[1] or i[0] == N - 1 - i[1])

# version 2
s = 1
num = 1
inc = 2
while inc < N:
    for i in range(4):
      num += inc
      s += num
    inc += 2
print s

# 669171001
