import copy
from random import randrange
import copy
import random

from numpy import indices

from Functionality import No

class Assistant:
    @staticmethod
    def expand(no, problem, type):
        set_children = []
        possibilities = problem.actions(no, type)
        if possibilities:
            for actions in possibilities:
                no_children = No()
                no_children._init_(possibilities[actions], no, no.cost + problem.step_cost, no.depth + 1)
                set_children.append(no_children)
        return set_children

    indice = 8
    initial_state = [['x'] * indices for _ in range(indice)]

    @staticmethod
    def matrizprint(matriz):
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                print(matriz[i][j], end="")
            print()
        print("\n")

    @staticmethod
    def ways(no):
        ways = []
        while no:
            ways.append(no)
            no = no.dad
        return ways

    @staticmethod
    def detects(aux_matriz, line, column):
        cont = 0
        for l in range(len(aux_matriz)):
            if aux_matriz[l][column] == aux_matriz[line][column]:
                cont += 1
            for c in range(len(aux_matriz)):
                if line == l:
                    if aux_matriz[line][c] == aux_matriz[line][column]:
                        cont += 1

        c = column
        for l in range(line, len(aux_matriz), 1):
            if c != len(aux_matriz):
                if aux_matriz[line][column] == aux_matriz[l][c]:
                    cont += 1
                c += 1

        c = column
        for l in range(line, -1, -1):
            if c != -1:
                if aux_matriz[line][column] == aux_matriz[l][c]:
                    cont += 1
                c -= 1

        c = column
        for l in range(line, len(aux_matriz), 1):
            if c != -1:
                if aux_matriz[line][column] == aux_matriz[l][c]:
                    cont += 1
                c -= 1

        c = column
        for l in range(line, -1, -1):
            if c != len(aux_matriz):
                if aux_matriz[line][column] == aux_matriz[l][c]:
                    cont += 1
                c += 1

        return cont - 6

    @staticmethod
    def achaQ(matriz, col):
        for line in range(len(matriz)):
            if matriz[line][col] == 'Q':
                return line

    @staticmethod
    def ColumnX(matriz, column):
        for line in range(len(matriz)):
            matriz[line][column] = 'x'
        return matriz

    def conflicts(self, board):
        conflicts = copy.deepcopy(board)
        for col in range(len(conflicts)):
            matriz = copy.deepcopy(board)
            matriz = self.ColumnX(matriz, col)
            for lin in range(len(conflicts)):
                matriz[lin][col] = 'Q'
                beats = self.detects(matriz, lin, col)
                matriz = self.ColumnX(matriz, col)
                aux = copy.deepcopy(matriz)
                for prox_col in range(len(conflicts)):
                    if prox_col != col:
                        line = self.achaQ(aux, prox_col)
                        beats += self.detects(aux, line, prox_col)
                        aux = self.ColumnX(aux, prox_col)
                conflicts[lin][col] = beats
                beats = 0
        return conflicts

    def bestSon(self, matriz):
        minor = 100
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if minor > matriz[i][j]:
                    minor = matriz[i][j]
        li_minor = []
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if matriz[i][j] == minor:
                    li_minor.append(matriz[i][j])
        return li_minor, minor

    def generateCost(self, conflicts, matriz):
        return conflicts[self.achaQ(matriz, 0)][0]

    def neighbors(self, matriz):
        neighbors = []
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if matriz[i][j] != 'Q':
                    aux = copy.deepcopy(matriz)
                    aux = self.ColumnX(aux, j)
                    aux[i][j] = 'Q'
                    neighbors.append(aux)
        return neighbors

    Beats = []
    visited = []

    def expandSite(self, no):
        aux = copy.deepcopy(no.state)
        li_minor, minor = self.bestSon(Assistant.Beats)
        select = random.randrange(0, len(li_minor))
        counter = -1
        for i in range(len(aux)):
            for j in range(len(aux)):
                if minor == Assistant.Beats[i][j]:
                    counter += 1
                if counter == select:
                    line = self.achaQ(aux, j)
                    aux[line][j] = 'x'
                    aux[i][j] = 'Q'
                    Assistant.Beats = self.conflicts(aux)
                    no_children = No()
                    no_children._init_(aux, no, self.generateCost(Assistant.Beats, aux), no.depth + 1)
                    return no_children

    def Peturbar(self, no):
        neighbors = self.neighbors(no.state)
        while True:
            select = random.randrange(0, len(neighbors))
            if neighbors[select] not in Assistant.visited:
                Assistant.visited.append(neighbors[select])
                break
        next = No()
        next._init_(neighbors[select], no, self.generateCost(self.conflicts(neighbors[select]), neighbors[select]),
                       no.depth + 1)
        return next

    @staticmethod
    def selectMask():
        a = random.randrange(0, 3)
        if a == 0:
            return [0, 0, 0, 0, 1, 1, 1, 1]
        if a == 1:
            return [1, 1, 1, 0, 0, 0, 0, 0]
        if a == 2:
            return [1, 1, 0, 0, 0, 0, 1, 1]
