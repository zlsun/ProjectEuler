#-*- encoding: utf-8 -*-
"""
Path sum: two ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.


$$

\begin{pmatrix}

\color{red}{131} & 673 & 234 & 103 & 18\\

\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & 150\\

630 & 803 & \color{red}{746} & \color{red}{422} & 111\\

537 & 699 & 497 & \color{red}{121} & 956\\

805 & 732 & 524 & \color{red}{37} & \color{red}{331}

\end{pmatrix}

$$


Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
"""

from utils import *

M = [map(int, l.split(',')) for l in file('./081_matrix.txt')]
L = len(M)

DP = [[0] * L for _ in range(L)]

for i in range(L):
    DP[0][i] = sum(M[0][:i + 1])
    DP[i][0] = sum(transpose(M)[0][:i])
for i in range(1, L):
    for j in range(1, L):
        DP[i][j] = min(DP[i - 1][j], DP[i][j - 1]) + M[i][j]

print DP[-1][-1]

# 427337
