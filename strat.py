import random

starting_amm = int(input(("what is the input")))
times_rolled = int(input("How many times do you play"))

win = 0.474


current_amm = starting_amm


for i in range (0,times_rolled):
    random.seed()
    temp = random.random()
    print(temp)
    if temp < 0.474 :
        print("win")
        starting_amm = 
    else:
        print("lose")
        starting_amm *= 2
        
    