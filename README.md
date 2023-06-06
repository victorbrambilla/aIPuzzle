Local Search Algorithms
This repository contains Python code for implementing local search algorithms. It includes the following algorithms:

Hill Climbing
Simulated Annealing
Genetic Algorithms
Getting Started
Prerequisites
To run the code, you need to have Python installed on your system. The code is compatible with Python 3.x.

Installation
Clone the repository to your local machine or download the ZIP file and extract its contents.

Open a terminal or command prompt and navigate to the project directory.

Install the required dependencies by running the following command:

Copy code
pip install numpy
Usage
Import the necessary modules and classes:

python
Copy code
from calendar import LocaleHTMLCalendar
import locale
from Functionality import No
from FunctionsToHelp import Assistant
import random
from random import randrange
import copy
import numpy
from operator import attrgetter
Create an instance of the LocalSearch class and call the desired search algorithm method:

python
Copy code
local_search = LocalSearch()
local_search.Hill_Climbing()
local_search.Simulated(T, interactions, pulos, coef)
local_search.Genetic_algorithms(n, election, repro, mut)
Adjust the algorithm parameters according to your needs. For example, in the Simulated method, T represents the initial temperature, interactions is the number of interactions per temperature, pulos is the number of consecutive successful interactions before decreasing the temperature, and coef is the cooling coefficient.

The algorithm will execute and display the output, including the final state, total depth, and cost.

Contributing
Contributions to this repository are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
