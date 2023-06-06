from Functionality import No
from FunctionsToHelp import Assistant
from random import randrange
import copy

class Queen:
    # variables used in local search
    initial_state = [] # generate initial array
    indice = 8
    for l in range(indice):
        line = []
        for c in range(indice):
            line.append("'x'")
        initial_state.append(line)


    def objective_test(self, no, type):
        if(type == "blind"): #Test for blind searches
            matriz = no.state
            cont = 0
            for l in range(len(matriz)):
                for c in range(len(matriz)):
                    if (matriz[l][c]=="'Q'"):
                        cont+=1
            if(cont == len(matriz)):
                 return True
            return False

    def action(self, no, Search):
        vector = []#vector of childrens
        if(Search == "blind"):# If blind search
            matriz = no.state
            column = no.depth
            for line in range(len(matriz)):
                matriz[line][column] = "'Q'"
                Beats = Assistant.detects(self, matriz, line, column)
                if(Beats==0): #Nao ocorreu conflicts
                    aux = copy.deepcopy(matriz)
                    vector.append(aux) #Vector of childrens
                matriz[line][column] = "'x'"
            return vector