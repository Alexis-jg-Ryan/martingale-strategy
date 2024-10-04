import random

def spin_roulette():
    roulette_colors = ['red'] * 18 + ['black'] * 18 + ['green']
    i = random.randint(0, 36)
    #print(f"radomint: {i}")
    return roulette_colors[i]

def martingale_strategy(starting_balance, initial_bet, max_spins):
    balance = starting_balance
    current_bet = initial_bet
    bank = 0

    for i in range(max_spins):
        outcome = spin_roulette()
        #print(f"Spin {i + 1}: The ball landed on {outcome}.")

        if outcome == 'red':  # Win condition
            #print(f"You gain ${current_bet}.")
            balance += current_bet
            current_bet = initial_bet  # Reset the bet after a win
        else:
            #print(f"You lose ${current_bet}.")
            balance -= current_bet
            current_bet *= 2  # Double the bet after a loss

        if balance < current_bet:
            #print("not enough for the next bet.")
            break

        if balance > starting_balance:  # bank the profit
            bank += initial_bet
            balance -= initial_bet

        #print(f"Current balance: ${balance}\n")

   #print(f"Final balance: ${balance}, final bank: {bank}")

    return balance, bank

# Test execution
starting_balance = 1000
initial_bet = 10
max_spins = 500
sessions = 5

total_balance = 0
total_bank = 0

for i in range(sessions):
    balance, bank = martingale_strategy(starting_balance, initial_bet, max_spins)
    total_balance += balance
    total_bank += bank

print(f"After {sessions} sessions(${starting_balance * sessions}):")
print(f"Total balance: ${total_balance}")
print(f"Total bank: ${total_bank}")



       


