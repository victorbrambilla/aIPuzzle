from FunctionsToHelp import Problems, No, Assistant
from Search.TypeEasySearch import TypeEasysearch
from Search.LocalSearch import LocalSearch
from SchemaForTheProblems.Puzzle import Puzzle
from SchemaForTheProblems.Queen import Queen
import time


class Main:
    def executar(self):
        ini = time.time() #Time
        Select = Queen() #Select which problem will be solved

        #Assembling the problem with the attributes of the problem
        problem = Problems()
        problem.init(Select.initial_state, Select.action, Select.objective_test, 1)

        #Select the type of search, TypeEasysearch or local
        # If searching with limited depth, it is necessary to specify the limit in the parameter
        # Local searches can only be used on Queens
        # ways = TypeEasysearch.depth_search(self, problem)
        print("Solving.....")
        ways = Local.Genetic_algorithms(self,100,10,80,10)
        fim = time.time()
        print("Time:", fim - ini)
        return ways

Exe = Main()
A = Exe.executar()
