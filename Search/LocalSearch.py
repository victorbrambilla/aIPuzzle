from calendar import LocaleHTMLCalendar
import locale
from Functionality import No
from FunctionsToHelp import Assistant
import random
from random import randrange
import copy
import numpy
from operator import attrgetter

class LocalSearch:
   
    def Hill_Climbing(self): #Subida da encosta
        matriz = [["'x'","'x'","'x'","'x'","'x'","'x'","'x'","'x'"],
                  ["'x'","'x'","'x'","'x'","'x'","'x'","'x'","'x'"],
                  ["'x'","'x'","'x'","'x'","'x'","'x'","'x'","'x'"],
                  ["'x'","'x'","'x'","'Q'","'x'","'x'","'x'","'x'"],
                  ["'Q'","'x'","'x'","'x'","'Q'","'x'","'x'","'x'"],
                  ["'x'","'Q'","'x'","'x'","'x'","'Q'","'x'","'Q'"],
                  ["'x'","'x'","'Q'","'x'","'x'","'x'","'Q'","'x'"],
                  ["'x'","'x'","'x'","'x'","'x'","'x'","'x'","'x'"]]
        # matriz = problem.initial_state # Gerar matriz automatica
        # for c in range(len(matriz)):
        #     n= randrange(0,7)
        #     matriz[n][c] = "'Q'"
        Assistant.Beats = Assistant.conflicts(self, matriz)
        Nos = No()
        Nos._init_(matriz,None,Assistant.generateCost(self, Assistant.Beats, matriz), 0) #No inicial
        for i in range(1000):
            if(Nos.cost<=0):
                break
            Nos = Assistant.expandSite(self, Nos)
        Assistant.matrizprint(self,Nos.state)
        print("Total Depth:", Nos.depth)
        return Assistant.ways(self,Nos)

    def Simulated(self,T,interactions, pulos, coef): #Recozimento Simulado
        matriz = [["'x'","'x'","'x'","'x'","'x'","'x'","'x'","'x'"],
                ["'x'","'x'","'x'","'x'","'x'","'x'","'x'","'x'"],
                ["'x'","'x'","'x'","'x'","'x'","'x'","'x'","'x'"],
                ["'x'","'x'","'x'","'Q'","'x'","'x'","'x'","'x'"],
                ["'Q'","'x'","'x'","'x'","'Q'","'x'","'x'","'x'"],
                ["'x'","'Q'","'x'","'x'","'x'","'Q'","'x'","'Q'"],
                ["'x'","'x'","'Q'","'x'","'x'","'x'","'Q'","'x'"],
                ["'x'","'x'","'x'","'x'","'x'","'x'","'x'","'x'"]]
        # matriz = problem.initial_state # Gerar matriz automatica
        # for c in range(len(matriz)):
        #     n= randrange(0,7)
        #     matriz[n][c] = "'Q'"
        Assistant.Beats = Assistant.conflicts(self, matriz)
        Nos = No()
        Nos._init_(matriz,None,Assistant.generateCost(self, Assistant.Beats, matriz), 0) #No inicial
        Assistant.matrizprint(self,Nos.state)
        for i in range(1000):
            nSucesso = 0
            for i in range(interactions):
                if(len(Assistant.visited)==56):
                    break
                Next = Assistant.Peturbar(self, Nos)
                Delta = Next.cost - Nos.cost
                if(Delta<=0 or numpy.exp(-Delta/T)>1):
                    Nos = Next
                    Assistant.visited =  []
                    nSucesso +=1
                if(nSucesso>=pulos):
                    break
            T = T*coef
            if(nSucesso==0 or Nos.cost<=0 or T<1):
                break
        Assistant.matrizprint(self,Nos.state)
        print("Total Depth:", Nos.depth)
        print("Cost:", Nos.cost)
        return Nos

    def Genetic_algorithms(self, n, election,repro,mut):
        population = locale.Generate_population(self, n)
        while(True):
            new_population = []
            if(Local.generic(self,population) == True):
                break

            for i in range(int(((n*election)/100))):
                new_population.append(copy.deepcopy(population[i]))

            while(len(new_population)<int(((n*(repro+election))/100))):
                random.shuffle(population)
                a = Local.rodeo(self,population)
                b = Local.rodeo(self,population)
                while(a==b):
                    b = Local.rodeo(self,population)
                lista1 = copy.deepcopy(Assistant.initial_state)
                lista2 = copy.deepcopy(Assistant.initial_state)
                mask = randrange(0,6)
                for col in range(len(lista1)):
                    if(col<=mask):
                        lista1[Assistant.achaQ(self,population[a].state,col)][col] = "'Q'"
                        lista2[Assistant.achaQ(self,population[b].state,col)][col] = "'Q'"
                    else:
                        lista1[Assistant.achaQ(self,population[b].state,col)][col] = "'Q'"
                        lista2[Assistant.achaQ(self,population[a].state,col)][col] = "'Q'"
                f1 = Local.expand(self,lista1)
                f2 = Local.expand(self,lista2)
                new_population.append(f1)
                new_population.append(f2)

            for i in range(int(((n*mut)/100))):
                random.shuffle(population)
                p = Local.rodeo(self,population)
                No = copy.deepcopy(population[p])
                c = randrange(0,7)
                line = Assistant.achaQ(self, No.state, c)
                l = randrange(0,7)
                No.state[line][c] = "'x'"
                No.state[l][c] = "'Q'"
                No.cost = Assistant.generateCost(self,Assistant.conflicts(self,No.state), No.state)
                new_population.append(No)

            population = copy.deepcopy(new_population)
        return population
    
    def Generate_population(self, n):
        population = []
        for k in range(n):
            matriz = copy.deepcopy(Assistant.initial_state)
            for col in range(8):
                select = randrange(0,7)
                matriz[select][col]="'Q'"
            Individual = Local.expand(self, matriz)
            population.append(Individual)
        return population

    def generic(self, population):
        population.sort(key=attrgetter("cost"))
        if(population[0].cost == 0):
            Assistant.matrizprint(self,population[0].state)
            print("Total Depth:", population[0].depth)
            print("Cost:", population[0].cost)
            return True

    def expand(self, lista):
        matriz = copy.deepcopy(lista)
        noSon = No()
        noSon._init_(matriz,None,Assistant.generateCost(self, Assistant.conflicts(self,matriz), matriz), None)
        return noSon

    def rodeo(self, population):
        lista=[]
        for i in range(3):
            p = randrange(0,len(population))
            lista.append(population[p])
        lista.sort(key=attrgetter("cost"))
        for i in range(len(population)):
            if(lista[0].cost==population[i].cost):
                return i