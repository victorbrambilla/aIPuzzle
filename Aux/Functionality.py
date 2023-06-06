import copy
from random import*
class Problems: #Caracteristicas do problem que será executado
    def _init_(self, initial_state, actions, objective_test, step_cost):
        self.initial_state = initial_state
        self.actions = actions
        self.objective_test = objective_test
        self.step_cost = step_cost

class No: #Caracteristicas da Posicao
    def _init_(self, state, dad, cost, depth):
        self.state = state
        self.dad = dad
        self.cost = cost
        self.depth = depth
    
