import random

def spin_roulette():
    roulette_colors = ['red'] * 18 + ['black'] * 18 + ['green']
    i = random.randint(0, 36)
    #print(f"radomint: {i}")
    return roulette_colors[i]

def martingale_strategy(starting_balance, initial_bet, max_spins):
    balance = starting_balance
    win_count = 0
    current_bet = initial_bet
    bank = 0

    for i in range(max_spins):
        outcome = spin_roulette()
        print(f"Spin {i+ 1}: The ball landed on {outcome}.")

        if outcome == 'red':  # Win condition
            print(f"You win! You gain ${current_bet}.")
            balance += current_bet  # Add the bet amount to the balance on win
            win_count += 1
            current_bet = initial_bet  # Reset the bet to the initial value after a win

        else:  # Lose condition
            print(f"You lose! You lose ${current_bet}.")
            balance -= current_bet  # Deduct the current bet from balance
            current_bet *= 2  # Double the bet for the next round

        # If we can't afford the next bet, exit
        if balance < current_bet:
            print("Insufficient balance for the next bet.")
            break

        if(balance > starting_balance):
            bank += initial_bet
            balance -= initial_bet
        
        print(f"Current balance: ${balance}\n")

    print(f"Final balance: ${balance}, final bank: {bank}")

    return balance,bank

# Parameters
starting_balance = 1000
initial_bet = 10
max_spins = 500  

# To store the cumulative totals across all attempts
total_balance = 0
total_bank = 0
sessions = 1

for i in range(sessions):
    balance, bank = martingale_strategy(starting_balance, initial_bet, max_spins)
    total_balance += balance  # Accumulate the final balance
    total_bank += bank  # Accumulate the final bank

# After all attempts, print the total balance and bank
print(f"After {sessions} attempts:")
print(f"Total balance: ${total_balance}")
print(f"Total bank: ${total_bank}")



       


