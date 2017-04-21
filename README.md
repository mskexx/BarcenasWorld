# Barcenas World Problem
### Aprendizaje y razonamiento automatico 2017
> Universitat de Lleida


### Prerequisites

Pycosat


## Running

```
./barcenas_world  size [x1,y1,s1,m1,c1] [x2,y2,s2,m2,c2] ...
```

## License
GPL 3.0

## Acknowledgments

In order to find Barcenas, following a given steps we recollect some
information about his position. Mariano and Cospedal will add extra info
of the suspect position

Every info collected is added into a CNF used by pycosat.

### IMPORTANT INFORMATION ABOUT SCHEMA:
In order to use SAT Solver, we assign every position on the map with a number  
Starting from left bot position and finishing in top right position.

For example in a 6x6 world:
POSITIONS  

| C1 | C2 | C3 | C4 | C5 | C6 |
| -- | -- | -- | -- | -- | -- |
| 6  | 12 | 18 | 24 | 30 | 36 |
| 5  | 11 | 17 | 23 | 29 | 35 |
| 4  | 10 | 16 | 22 | 28 | 34 |
| 3  | 9  | 15 | 21 | 27 | 33 |
| 2  | 8  | 14 | 20 | 26 | 32 |
| 1  | 7  | 13 | 19 | 25 | 31 |  


The position is introduced by coords:  
>(1,1) = 1  
>(3,4) = 16  

Obtaning the position:  
```
pos = size * (coord_x -1) + coord_y
```
### Examples
Mariano found in (2,2) and Cospedal in (2,3)  
 ```
 ./barcenas_world.py 6 [1,1,0,-1,-1] [1,2,0,-1,-1] [2,2,0,1,-1] [2,3,0,-1,1]  
 ```

 Smell Barcenas in (4,5)  
 ```
 ./barcenas_world.py 8 [1,1,0,-1,-1] [2,1,0,-1,-1] [3,1,0,-1,-1] [3,2,0,-1,-1] [3,3,0,-1,-1] [3,4,0,-1,-1] [3,5,0,-1,-1] [4,5,1,-1,-1]  

 ```
Obtaning the position:
```
pos = size * (coord_x -1) + coord_y

```


# Example Executions:
## TEST 1
###### Input
```
./barcenas_world.py 6 [1,1,0,-1,-1] [1,2,0,-1,-1] [2,2,0,1,-1] [2,3,0,-1,1]

```
###### Output
+--+ THIS IS THE INITIAL STATE OF BARCENAS WORLD +--+  

| C1 | C2 | C3 | C4 | C5 | C6 |
| -- | -- | -- | -- | -- | -- |
| 1  | 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  | 1  |
| 0  | 1  | 1  | 1  | 1  | 1  |  


--> Processing position (1,1)  
-- ACTUAL MAP STATUS --  

| C1 | C2 | C3 | C4 | C5 | C6 |
| -- | -- | -- | -- | -- | -- |
| 1  | 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  | 1  |
| 0  | 1  | 1  | 1  | 1  | 1  |
| 0  | 0  | 1  | 1  | 1  | 1  |  


--> Processing position (1,2)  
-- ACTUAL MAP STATUS --  

| C1 | C2 | C3 | C4 | C5 | C6 |
| -- | -- | -- | -- | -- | -- |
| 1  | 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  | 1  |
| 0  | 1  | 1  | 1  | 1  | 1  |
| 0  | 0  | 1  | 1  | 1  | 1  |
| 0  | 0  | 1  | 1  | 1  | 1  |  


--> Processing position (2,2)  
-- Mariano says Barcenas is on direction 1 from position num: 8  
-- ACTUAL MAP STATUS --  

| C1 | C2 | C3 | C4 | C5 | C6 |
| -- | -- | -- | -- | -- | -- |
| 1  | 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  | 1  |
| 0  | 0  | 1  | 1  | 1  | 1  |
| 0  | 0  | 0  | 1  | 1  | 1  |
| 0  | 0  | 1  | 1  | 1  | 1  |  



--> Processing position (2,3)  
-- Cospedal says Mariano LIED --  
-- ACTUAL MAP STATUS --  

| C1 | C2 | C3 | C4 | C5 | C6 |
| -- | -- | -- | -- | -- | -- |
| 0  | 0  | 1  | 1  | 1  | 1  |
| 0  | 0  | 1  | 1  | 1  | 1  |
| 0  | 0  | 1  | 1  | 1  | 1  |
| 0  | 0  | 0  | 1  | 1  | 1  |
| 0  | 0  | 0  | 1  | 1  | 1  |
| 0  | 0  | 1  | 1  | 1  | 1  |  



## TEST 2
###### Input
```
 ./barcenas_world.py 5 [1,1,0,-1,-1] [2,1,0,-1,-1] [3,1,0,-1,-1] [3,2,0,-1,-1] [3,3,0,-1,-1] [3,4,0,-1,-1] [3,5,1,-1,-1]  

```
###### Output
+--+ THIS IS THE INITIAL STATE OF BARCENAS WORLD +--+  

| C1 | C2 | C3 | C4 | C5 |
| -- | -- | -- | -- | -- |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  |
| 0  | 1  | 1  | 1  | 1  |



--> Processing position (1,1)  
-- ACTUAL MAP STATUS --  

| C1 | C2 | C3 | C4 | C5 |
| -- | -- | -- | -- | -- |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  |
| 0  | 1  | 1  | 1  | 1  |
| 0  | 0  | 1  | 1  | 1  |


--> Processing position (2,1)  
-- ACTUAL MAP STATUS --  

| C1 | C2 | C3 | C4 | C5 |
| -- | -- | -- | -- | -- |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  |
| 0  | 0  | 1  | 1  | 1  |
| 0  | 0  | 0  | 1  | 1  |

--> Processing position (3,1)  
-- ACTUAL MAP STATUS --  
| C1 | C2 | C3 | C4 | C5 |
| -- | -- | -- | -- | -- |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  |
| 0  | 0  | 0  | 1  | 1  |
| 0  | 0  | 0  | 0  | 1  |

--> Processing position (3,2)  
-- ACTUAL MAP STATUS --  

| C1 | C2 | C3 | C4 | C5 |
| -- | -- | -- | -- | -- |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 0  | 1  | 1  |
| 0  | 0  | 0  | 0  | 1  |
| 0  | 0  | 0  | 0  | 1  |

--> Processing position (3,3)  
-- ACTUAL MAP STATUS --  

| C1 | C2 | C3 | C4 | C5 |
| -- | -- | -- | -- | -- |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 0  | 1  | 1  |
| 1  | 0  | 0  | 0  | 1  |
| 0  | 0  | 0  | 0  | 1  |
| 0  | 0  | 0  | 0  | 1  |

--> Processing position (3,4)  
-- ACTUAL MAP STATUS --  

| C1 | C2 | C3 | C4 | C5 |
| -- | -- | -- | -- | -- |
| 1  | 1  | 1  | 1  | 1  |
| 1  | 1  | 0  | 1  | 1  |
| 1  | 0  | 0  | 0  | 1  |
| 1  | 0  | 0  | 0  | 1  |
| 0  | 0  | 0  | 0  | 1  |
| 0  | 0  | 0  | 0  | 1  |

--> Processing position (3,5)
-- ACTUAL MAP STATUS --
>NOTA: Sensor de olfato ha detectado aqui
| C1 | C2 | C3 | C4 | C5 |
| -- | -- | -- | -- | -- |
| 0  | 1  | 0  | 1  | 0  |
| 0  | 0  | 0  | 0  | 0  |
| 0  | 0  | 0  | 0  | 0  |
| 0  | 0  | 0  | 0  | 0  |
| 0  | 0  | 0  | 0  | 0  |
| 0  | 0  | 0  | 0  | 0  |
