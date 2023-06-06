from Functionality import No
from FunctionsToHelp import Assistant
import random
from operator import attrgetter
from random import randrange

class TypeEasysearch: #Searches separated by functions

    def depth_search(self,problem):
        edge = [] #List of Nodes
        Nos = No()
        Nos._init_(problem.initial_state,None, 0, 0) #InitialNo
        edge.insert(0,Nos) #Inserting
        while(True):
            Assistant.matrizprint(self,edge[0].state)
            if(problem.objective_test(edge[0],"blind") == True ):#Achieve the objective
                print("Total Depth:", edge[0].depth)
                return Assistant.ways(self,edge[0])
            childrens = Assistant.expand(self,edge[0], problem,"blind") #Expand
            edge.pop(0)#remover da edge
            for actions in range(len(childrens)):
                 edge.insert(0,childrens[actions]) # Insert at beginning
    
    def breadth_search(self, problem):
        edge = [] #List of Nodes
        Nos = No()
        Nos._init_(problem.initial_state,None, 0, 0) #InitialNo
        edge.insert(0,Nos) 
        while(True):
            Assistant.matrizprint(self,edge[0].state)
            if(problem.objective_test(edge[0],"blind") == True ): #Achieve the objective
                print("Total Depth:", edge[0].depth)
                return Assistant.ways(self,edge[0])
            childrens = Assistant.expand(self,edge[0], problem,"TypeEasysearch") #Expand
            #random.shuffle(childrens)
            edge.pop(0) #remove from edge
            for actions in range(len(childrens)):
                 edge.append(childrens[actions]) #Insert at end
       

    def limited_depth_search(self, problem,limite):
        edge = [] #List of Nodes
        Nos = No()
        Nos._init_(problem.initial_state,None, 0, 0) #InitialNo
        edge.insert(0,Nos) #Inserting
        while(True):
            if(edge==[]):
                print("Not reached this limit")
                return 0, False #Boolean used in interactive search
            Assistant.matrizprint(self,edge[0].state)
            if(problem.objective_test(edge[0],"blind") == True ):   #Achieve the objective
                print("Total Depth:", edge[0].depth)
                return Assistant.ways(self,edge[0]), True #Boolean used in interactive search
            if(edge[0].depth<limite):
                childrens = Assistant.expand(self,edge[0], problem,"blind") #Expandir
                random.shuffle(childrens) 
                edge.pop(0) 
                for actions in range(len(childrens)):
                    edge.insert(0,childrens[actions])
            else:
                edge.pop(0)
    
    def interactive_deep_search(self, problem):
        interaction = 0 #Number of interactions
        while(True): #Stay in a loop until the user wants to stop
            ways, resultado = TypeEasysearch.limited_depth_search(self,problem, interaction)
            interaction+=1
            if(resultado == True):
                return ways
            print("---------------------------------")
    
    def depth_search_with_visitor_list(self,problem):
        edge = [] #List of Nodes
        visited = []
        Nos = No()
        Nos._init_(problem.initial_state,None, 0, 0) #InitialNo
        edge.insert(0,Nos) #Inserting
        while(True):
            Assistant.matrizprint(self,edge[0].state) 
            if(edge==[]):
                print("Total Depth:", edge[0].depth)
                return Assistant.ways(self,edge[0])
            if(problem.objective_test(edge[0],"blind") == True ):#Achieve the objective
                print("Total Depth:", edge[0].depth)
                return Assistant.ways(self,edge[0])
            while(True): #Check if the node has already been visited
                if not edge[0] in visited:
                    visited.append(edge[0])
                    break
                edge.pop(0)
            childrens = Assistant.expand(self,edge[0], problem,"blind") #Expandir
            random.shuffle(childrens)   
            edge.pop(0)
            for actions in range(len(childrens)):
                 edge.insert(0,childrens[actions]) 
    
    def busca_com_custo_uniforme(self, problem):
        edge = [] 
        Nos = No()
        Nos._init_(problem.initial_state,None, 0, 0)    
        edge.insert(0,Nos)  
        while(True):
            Assistant.matrizprint(self,edge[0].state)
            if(problem.objective_test(edge[0],"blind") == True ): #Achieve the objective
                return Assistant.ways(self,edge[0])
            childrens = Assistant.expand(self,edge[0], problem,"blind") 
            edge.sort(key=attrgetter("path_cost"))
            edge.pop(0)
            for actions in range(len(childrens)):
                 edge.append(childrens[actions])