# Local Search Algorithms

This repository contains Python code for implementing local search algorithms. It includes the following algorithms:

- Hill Climbing
- Simulated Annealing
- Genetic Algorithms

## Getting Started

### Prerequisites

To run the code, you need to have Python installed on your system. The code is compatible with Python 3.x.

### Installation

1. Clone the repository to your local machine or download the ZIP file and extract its contents.
  
git clone https://github.com/YasminAlmeida/aIPuzzle.git
  

2. Open a terminal or command prompt and navigate to the project directory.

3. Install the required dependencies by running the following command:

shell
pip install numpy


### Usage

1. Import the necessary modules and classes:

python
from calendar import LocaleHTMLCalendar
import locale
from Functionality import No
from FunctionsToHelp import Assistant
import random
from random import randrange
import copy
import numpy
from operator import attrgetter


2. Create an instance of the LocalSearch class and call the desired search algorithm method:
python
Copy code
local_search = LocalSearch()
local_search.Hill_Climbing()
local_search.Simulated(T, interactions, pulos, coef)
local_search.Genetic_algorithms(n, election, repro, mut)

## Hill Climbing
Hill Climbing - It is a repetitive loop that steadily moves towards feasible solutions. As the iterations progress, the algorithm tends to move towards a chessboard configuration where there are no attacks between the queens. In the figure below, you can see an example of how the algorithm solves the eight queens problem. The numbers on the chessboard represent the direct and indirect attacks based on their positions, and the gray background represents the best positions.

## Simulated Annealing 
Simulated Annealing - This algorithm addresses the issue of getting stuck in local minima, which can happen in Hill Climbing. It achieves this by not always choosing the best move, but instead selecting a random move. If the random move improves the situation, it is accepted. However, if it worsens the situation, it may still be accepted based on a probability that decreases over time. This allows the algorithm to explore different areas of the search space and potentially find better solutions.

## Genetic Algorithms
Genetic Algorithms - This algorithm is based on a population of randomly generated states, called individuals. Each individual represents a possible arrangement of the queens on a chessboard. The algorithm evolves this population through several stages, as shown in the figure below. These stages involve processes such as selection, crossover, and mutation, which mimic the principles of natural selection and genetic variation. By iteratively applying these processes, the algorithm aims to find better and better solutions over time.


Adjust the algorithm parameters according to your needs. For example, in the Simulated method, T represents the initial temperature, interactions is the number of interactions per temperature, pulos is the number of consecutive successful interactions before decreasing the temperature, and coef is the cooling coefficient.

The algorithm will execute and display the output, including the final state, total depth, and cost.


## Contributing
Victor Brambilla,
Yasmin Almeida.
