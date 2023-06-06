from FunctionsToHelp import No
import copy

class Puzzle:
    
    initial_state = [[2, 3, 1], [5, 8, 7], [6, 4, 0]]

    def initial_test(self, no):
        return no.state == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def objective_test(self, no):
        return no.state == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def acao(self, no):
        l, c = 0, 0
        puzzle = no.state
        vector = []

        for i in range(3):
            for j in range(3):
                if puzzle[i][j] == 0:
                    l = i
                    c = j
        # Move right        
        if c != 2:
            aux = copy.deepcopy(puzzle)
            aux[l][c] = puzzle[l][c + 1]
            aux[l][c + 1] = puzzle[l][c]
            vector.append(aux)

        # Move left
        if c != 0:
            aux = copy.deepcopy(puzzle)
            aux[l][c] = puzzle[l][c - 1]
            aux[l][c - 1] = puzzle[l][c]
            vector.append(aux)

        # Move up
        if l != 0:
            aux = copy.deepcopy(puzzle)
            aux[l][c] = puzzle[l - 1][c]
            aux[l - 1][c] = puzzle[l][c]
            vector.append(aux)

        # Mover down
        if l != 2:
            aux = copy.deepcopy(puzzle)
            aux[l][c] = puzzle[l + 1][c]
            aux[l + 1][c] = puzzle[l][c]
            vector.append(aux)

        return vector
