# Barcenas World Problem
###Aprendizaje y razonamiento automatico 2017
> Universitat de LLeida


### Prerequisites

Pycosat


## Running
./barcenas_world  size [x1,y1,s1,m1,c1] [x2,y2,s2,m2,c2] ...

## License
GPL 3.0

## Acknowledgments

In order to find Barcenas, following a given steps we recollect some
information about his position. Mariano and Cospedal will add extra info
of the suspect position

Every info collected is added into a CNF used by pycosat.

###IMPORTANT INFORMATION ABOUT SCHEMA:
In order to use SAT Solver, we assign every position on the map with a number
Starting from left bot position and finishing in top right position.

For example in a 6x6 world:
POSITIONS
╔═══╦═══╦═══╦═══╦═══╦═══╗  
║ 6 ║12 ║18 ║24 ║30 ║36 ║  
╠═══╬═══╬═══╬═══╬═══╬═══╣  
║ 5 ║11 ║17 ║23 ║29 ║35 ║  
╠═══╬═══╬═══╬═══╬═══╬═══╣  
║ 4 ║10 ║16 ║22 ║28 ║34 ║  
╠═══╬═══╬═══╬═══╬═══╬═══╣  
║ 3 ║ 9 ║15 ║21 ║27 ║33 ║  
╠═══╬═══╬═══╬═══╬═══╬═══╣  
║ 2 ║ 8 ║14 ║20 ║26 ║32 ║  
╠═══╬═══╬═══╬═══╬═══╬═══╣  
║ 1 ║ 7 ║13 ║19 ║25 ║31 ║  
╚═══╩═══╩═══╩═══╩═══╩═══╝  

The position is introduced by coords:
>(1,1) = 1  
>(3,4) = 16  

Obtaning the position: pos = size * (coord_x -1) + coord_y
