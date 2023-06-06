from FunctionsToHelp import No  # Importing the No class from FunctionsToHelp module
from collections import ChainMap  # Importing the ChainMap class from collections module


class MapRomenia:
    def _init_(self):
        self.Arad = No("Arad", None)  # Creating an instance of No class with name "Arad"

        insert(self.Arad, No("Sibiu", self.Arad, 140))  # Inserting a new instance of No class into self.Arad
        insert(self.Arad, No("Zerind", self.Arad, 75))
        insert(self.Arad, No("Timisoara", self.Arad, 118))

        self.Timisoara = No("Timisoara", None)  # Creating an instance of No class with name "Timisoara"

        insert(self.Timisoara, No("Arad", self.Timisoara, 118))
        insert(self.Timisoara, No("Lugoj", self.Timisoara, 111))

        self.Zerind = No("Zerind", None)  # Creating an instance of No class with name "Zerind"

        insert(self.Zerind, No("Arad", self.Zerind, 75))
        insert(self.Zerind, No("Oradea", self.Zerind, 71))

        self.Oradea = No("Oradea", None)  # Creating an instance of No class with name "Oradea"

        insert(self.Oradea, No("Zerind", self.Oradea, 71))
        insert(self.Oradea, No("Sibiu", self.Oradea, 151))

        # ... (similar sections for other cities)

    def opcao(self):
        vetorTotal = ChainMap(
            {"Arad": self.Arad}, {"Sibiu": self.Sibiu}, {"Fagaras": self.Fagaras}, {"Bucharest": self.Bucharest},
            {"Rimnicu Vilcea": self.Rv}, {"Pitesti": self.Pitesti}, {"Zerind": self.Zerind},
            {"Oradea": self.Oradea}, {"Timisoara": self.Timisoara}, {"Lugoj": self.Lugoj}, {"Mehadia": self.Mehadia},
            {"Dobreta": self.Dobreta}, {"Craiova": self.Craiova}, {"Giurgiu": self.Giurgiu}, {"Urziceni": self.Urziceni},
            {"Hirsova": self.Hirsova}, {"Eforie": self.Eforie}, {"Vaslui": self.Vaslui}, {"Iasi": self.Iasi},
            {"Neamt": self.Neamt}
        )  # Creating a ChainMap of dictionaries containing city names as keys and their respective instances as values
        return vetorTotal


def insert(noExist, no):
    noExist.son.append(no)  # Appending the new instance of No class to the son attribute of the existing instance


# generate comments for this code
