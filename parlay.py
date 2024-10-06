import random

def spin_roulette():
    roulette_colors = ['red'] * 18 + ['black'] * 18 + ['green']
    i = random.randint(0, 36)  # Roulette has 37 numbers (0-36)
    return roulette_colors[i]

def parlay_strategy(starting_balance, initial_bet, max_spins):
    balance = starting_balance
    current_bet = initial_bet

    for i in range(max_spins):
        outcome = spin_roulette()

        if outcome == 'red':  # Win condition
            balance += current_bet
            current_bet *= 2  # Double the bet after a win
        else:
            balance -= current_bet
            current_bet = initial_bet  # Reset the bet after a loss

        if balance < current_bet:
            # Stop if balance is too low for the next bet
            break

        # Cap the bet size at 2^6 (to limit the risk)
        if current_bet >= initial_bet * 2**6:
            current_bet /= 2  # Reduce the bet to a safer amount

    return balance

# Test execution
starting_balance = 600
initial_bet = 5
max_spins = 500
sessions = 100

total_balance = 0

for i in range(sessions):
    balance = parlay_strategy(starting_balance, initial_bet, max_spins)
    total_balance += balance

print(f"After {sessions} sessions (${starting_balance * sessions} initial total):")
print(f"Total balance left: ${total_balance}")
