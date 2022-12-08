
# Description: This script will verify the drop rate of a shop 
# by running the simulator 100000 times and counting the number of times
# each champion is chosen.

from Simulator.player import player
from Simulator.pool import pool
from Simulator.champion import champion
from Simulator.pool import COST_1, COST_2, COST_3, COST_4, COST_5






#Verify shop drop rates for each cost are correct



def verifyShopDropRate():
    # Create a player and pool
    pool1 = pool()
    
    player1 = player(pool_pointer=pool1, player_num=1)
  
    
    


    
    
    #loop through 9 player levels 
    for i in range(1,10):
        player1.level = i
        costs = verify(pool1, player1)
        
        #what is the percentage of each cost chosen?
        
        print("Player level: " + str(i))
        
        total_1_cost = 0
        total_2_cost = 0
        total_3_cost = 0
        total_4_cost = 0
        total_5_cost = 0
        
        
        
        #loop though each cost 1 champion
        for j in range(len(costs[0])):
            print(str(list(costs[0])[j]) + ": " + str(costs[0][list(costs[0])[j]]/100000))
            total_1_cost += costs[0][list(costs[0])[j]]
            
        #loop though each cost 2 champion
        for j in range(len(costs[1])):
            print(str(list(costs[1])[j]) + ": " + str(costs[1][list(costs[1])[j]]/100000))
            total_2_cost += costs[1][list(costs[1])[j]]
       
        #loop though each cost 3 champion
        for j in range(len(costs[2])):
            print(str(list(costs[2])[j]) + ": " + str(costs[2][list(costs[2])[j]]/100000))
            total_3_cost += costs[2][list(costs[2])[j]]
            
        #loop though each cost 4 champion
        for j in range(len(costs[3])):
            print(str(list(costs[3])[j]) + ": " + str(costs[3][list(costs[3])[j]]/100000))
            total_4_cost += costs[3][list(costs[3])[j]]
            
        #loop though each cost 5 champion
        for j in range(len(costs[4])):
            print(str(list(costs[4])[j]) + ": " + str(costs[4][list(costs[4])[j]]/100000))
            total_5_cost += costs[4][list(costs[4])[j]]
            
        print("Drop rate 1 cost champion  : " + str(total_1_cost/100000))
        print("Drop rate 2 cost champion  : " + str(total_2_cost/100000))
        print("Drop rate 3 cost champion  : " + str(total_3_cost/100000))
        print("Drop rate 4 cost champion  : " + str(total_4_cost/100000))
        print("Drop rate 5 cost champion  : " + str(total_5_cost/100000))
        print("Total percent (should be 1.0 or very close)  : " + str((total_1_cost + total_2_cost + total_3_cost + total_4_cost + total_5_cost)/100000))
    

def verify(_pool, _player): 
    shop = pool.sample(self=_pool, player=_player, num=100000, idx=-1)
    

    
    #a dictionary to store the number of times each cost is chosen
    
    cost_1 = {}
    cost_2 = {}
    cost_3 = {}
    cost_4 = {}
    cost_5 = {}
    
    
    

    
    
    # the number of times each cost is chosen
    for i in range(len(shop)):
        if shop[i] in COST_1:
            if shop[i] in cost_1:
                cost_1[shop[i]] += 1
            else:
                cost_1[shop[i]] = 1
        elif shop[i] in COST_2:
            if shop[i] in cost_2:
                cost_2[shop[i]] += 1
            else:
                cost_2[shop[i]] = 1
        elif shop[i] in COST_3:
            if shop[i] in cost_3:
                cost_3[shop[i]] += 1
            else:
                cost_3[shop[i]] = 1
        elif shop[i] in COST_4:
            if shop[i] in cost_4:
                cost_4[shop[i]] += 1
            else:
                cost_4[shop[i]] = 1
        elif shop[i] in COST_5:
            if shop[i] in cost_5:
                cost_5[shop[i]] += 1
            else:
                cost_5[shop[i]] = 1
        else:
            print("ERROR: Champion not found in any cost")


    return cost_1, cost_2, cost_3, cost_4, cost_5
    