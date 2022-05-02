############################################################
# File:    project_Domino.py
# Author:  Y. Ukawa
# Date:    Apr 14, 2022
# Project: Tiling a grid with dominos
############################################################

from project_TableModule import Table

print("== Calculate the number of tilings of a grid (4 x W) with dominoes (2 x 1) ==")

print("\nEnter the number (1 ≤ n ≤ 1000) of datasets that follow:")
while True:
    n = int(input())
    if 1 <= n <= 1000:
        break
    print("Try again:")

result = []
print("\nEnter values for W ():")
for i in range(0, n):
    t = Table()
    t.placeDomino()
    result.append(t.count)

print("\nResults:")
for i in range(0, n):
    print(i + 1, result[i])
