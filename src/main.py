import random


def monty_hall_game(switch_doors: bool) -> bool:
    """Simulate one Monty Hall game and return whether the player wins."""
    doors = ["car", "goat", "goat"]
    random.shuffle(doors)

    initial_choice = random.randrange(len(doors))

    possible_reveals = [
        index
        for index, prize in enumerate(doors)
        if index != initial_choice and prize == "goat"
    ]

    revealed_door = random.choice(possible_reveals)

    if switch_doors:
        final_choice = next(
            index
            for index in range(len(doors))
            if index != initial_choice and index != revealed_door
        )
    else:
        final_choice = initial_choice

    return doors[final_choice] == "car"


def simulate_game_history(
    num_games: int,
) -> tuple[list[float], list[float]]:
    """Return cumulative win rates for both strategies after each game."""
    if isinstance(num_games, bool) or not isinstance(num_games, int):
        raise TypeError("num_games must be an integer.")

    if num_games <= 0:
        raise ValueError("num_games must be greater than zero.")

    stay_history = []
    switch_history = []

    stay_wins = 0
    switch_wins = 0

    for game_number in range(1, num_games + 1):
        if monty_hall_game(switch_doors=False):
            stay_wins += 1

        if monty_hall_game(switch_doors=True):
            switch_wins += 1

        stay_history.append(stay_wins / game_number)
        switch_history.append(switch_wins / game_number)

    return stay_history, switch_history


def simulate_game(num_games: int) -> tuple[float, float]:
    """Return final win rates for staying and switching."""
    stay_history, switch_history = simulate_game_history(num_games)

    return stay_history[-1], switch_history[-1]


def main() -> None:
    num_games = 1000
    stay_rate, switch_rate = simulate_game(num_games)

    print(f"Number of games: {num_games}")
    print(f"Win rate without switching: {stay_rate:.2%}")
    print(f"Win rate with switching: {switch_rate:.2%}")


if __name__ == "__main__":
    main()
