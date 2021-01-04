#Simulates out how often a streak of 6 of the same flip would occur in a coin flip game

import random

print("Input the number of coin flips for this simulation:")

simulations = input()
coinflip_list = []
streak = 0
streaks_num = 0


for i in range(0,int(simulations)): #creates list of coinflip results
    coinflip = random.randint(0,1)
    coinflip_list.append(coinflip)

    if i == 0: # checks for streaks
        pass

    elif coinflip_list[i] == coinflip_list[i - 1]:
        streak += 1
        if streak == 6:
            streaks_num += 1    
    else:
        streak = 0


print("This simulation found " + str(streaks_num) + " streaks of 6 consecutive heads or tails, which works out to " 
        + str(streaks_num / int(simulations) * 100) + '%.')




