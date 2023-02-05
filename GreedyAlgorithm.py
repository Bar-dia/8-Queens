#Greedy algorithm for n queens problem.
#The program prints the random state first and then the obtained state.

import random

#h(n)
def Collisions(State) :
    
    horizontal_collisions = int (sum ([State.count(queen)-1 for queen in State]) / 2)
    diagonal_collisions = 0
    
    for i in range (len (State) - 1) :
                
            for j in range (i + 1, len (State)) :
                    
                if abs (State [j] - State [i]) == abs (i - j) :
                    
                    diagonal_collisions += 1
                                 
    return horizontal_collisions + diagonal_collisions
                                        
#getting the size of the board           
n  = int (input ("Give the size of the board : "))

#defining the board
Board = [None] * n

for i in range (n) :
    
    Board [i] = random.randint (0, n - 1)

#random state is created
Random_State = Board

print(Random_State)

 #greedy algorithm based on h(n)
for i in range (n) :
    
    Best_Collision = 0
    Best_Position = 0
    
    for j in range (n) :
        
        Random_State [i] = j
        Temp_Collision = Collisions(Random_State)
        
        if (Temp_Collision < Best_Collision or Best_Collision == 0) :
            
            Best_Collision = Temp_Collision
            Best_Position = j
    
    Random_State [i] = Best_Position
    
print (Random_State)


    
    
            
        
        
        

