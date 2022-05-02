############################################################
# File:    project_TableModule.py
# Author:  Y. Ukawa
# Date:    Apr 14, 2022
# Project: Tiling a grid with dominos
############################################################

import copy

class Table:
    empty = [0, 0, 0, 0]
    table = []
    domino = 0
    count = 0

    def __init__(self):
        self.w = int(input())
        for j in range(0, self.w):
            self.table.append(copy.deepcopy(self.empty))
    
    def findEmptyCell(self):
        for i in range(0, self.w):
            for j in range(0, 4):
                if self.table[i][j] == 0:
                    return (i, j)
        return None

    def placeDomino(self):
        cell = self.findEmptyCell()
        if cell is None:
            # we have a full board with no empy cells
            self.count += 1
            return
        # try to put a new domino horizontally
        x = cell[0]
        y = cell[1]
        self.domino += 1
        self.table[x][y] = self.domino
        if y < 3 and self.table[x][y + 1] == 0:
            self.table[x][y + 1] = self.domino
            self.placeDomino()
            self.table[x][y + 1] = 0
        if x < self.w - 1 and self.table[x + 1][y] == 0:
            self.table[x + 1][y] = self.domino
            self.placeDomino()
            self.table[x + 1][y] = 0
        self.table[x][y] = 0
        self.domino -= 1
