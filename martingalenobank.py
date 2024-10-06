import random

def spin_roulette():
    roulette_colors = ['red'] * 18 + ['black'] * 18 + ['green']
    i = random.randint(0, 36)  # Corrected range to include 'green'
    return roulette_colors[i]

def martingale_strategy(starting_balance, initial_bet, max_spins):
    balance = starting_balance
    current_bet = initial_bet

    for i in range(max_spins):
        outcome = spin_roulette()

        if outcome == 'red':  # Win condition
            balance += current_bet
            current_bet = initial_bet  # Reset the bet after a win
        else:
            balance -= current_bet
            current_bet *= 2  # Double the bet after a loss

        if balance < current_bet:
            break

    return balance

# Test execution
starting_balance = 1000
initial_bet = 10
max_spins = 120
sessions = 100

total_balance = 0
total_bank = 0
actual_sessions = 0

for i in range(sessions):
    balance = martingale_strategy(starting_balance, initial_bet, max_spins)
    total_balance += balance
    actual_sessions += 1

print(f"After {actual_sessions} sessions (${starting_balance * sessions}):")
print(f"Total balance left: ${total_balance}")
       