import random

# Initialize counters for swapping and not swapping wins
swap_wins = 0
dont_swap_wins = 0

# Number of iterations (rounds)
num_trials = 1000

for _ in range(num_trials):
    doors = [0] * 3
    goatdoor = []

    # Randomly place the car behind one door
    car_position = random.randint(0, 2)
    doors[car_position] = "BWM"

    # Place goats behind the other doors
    for i in range(3):
        if i != car_position:
            doors[i] = "Goat"
            goatdoor.append(i)

    # Player makes an initial choice
    player_choice = random.randint(0, 2)

    # Host opens a door that has a goat, but not the player's chosen door
    door_open = random.choice(goatdoor)
    while door_open == player_choice:
        door_open = random.choice(goatdoor)

    # Simulate player's choice to swap or not
    should_swap = random.choice(['y', 'n'])  # Randomly decide whether to swap
    if should_swap == 'y':
        # Player swaps: choose the other unopened door
        new_choice = [i for i in range(3) if i != player_choice and i != door_open][0]
        if doors[new_choice] == "BWM":
            swap_wins += 1  # Player wins by swapping
    else:
        # Player does not swap, stick with the original choice
        if doors[player_choice] == "BWM":
            dont_swap_wins += 1  # Player wins by not swapping

# Display results
print(f"After {num_trials} trials:")
print(f"Swapping wins: {swap_wins}")
print(f"Not swapping wins: {dont_swap_wins}")
