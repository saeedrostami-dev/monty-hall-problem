# Monty Hall Problem

A Python simulation of the Monty Hall problem that compares the probability of winning when staying with the initial door choice versus switching to the other unopened door.

## About the Project

The Monty Hall problem is a probability puzzle based on a game show scenario.

There are three doors:
- One door hides a car.
- Two doors hide goats.

The player chooses one door. The host, who knows what is behind each door, opens another door that hides a goat. The player can then either keep the original choice or switch to the remaining unopened door.

Although switching may feel counterintuitive, it gives the player a higher probability of winning.

- **Stay with the initial choice:** approximately 1/3 probability of winning.
- **Switch to the other unopened door:** approximately 2/3 probability of winning.

This project simulates the game repeatedly to compare these strategies experimentally.

## Features

- Simulates individual Monty Hall games.
- Compares staying and switching strategies.
- Runs multiple simulations and calculates win rates.
- Validates simulation input.
- Includes automated tests using `pytest`.
- Uses `unittest.mock.patch` to test game logic under controlled conditions.

## Project Structure

```text
Monty Hall Problem/
├── README.md
├── src/
│   └── main.py
└── tests/
    └── test_monty_hall.py
```

## Requirements

- Python 3.12 or a compatible Python version
- pytest (for running tests)

## Run the Simulation

From the project root directory, run:

```bash
python src/main.py
```

The program simulates 1,000 games for each strategy and prints the resulting win rates.

Example output:

```text
Number of games: 1000
Win rate without switching: 33.20%
Win rate with switching: 66.80%
```

*The results are random and will vary between runs.*

## Run the Tests

Install pytest if it is not already installed:

```bash
python -m pip install pytest
```

Run the test suite from the project root directory:

```bash
python -m pytest -v
```

The tests cover invalid inputs, simulation behavior, and the four main win/loss scenarios for staying and switching.

## Concepts Practiced

- Python functions and return values
- Type hints
- Lists and list comprehensions
- `enumerate()`, `next()`, and generator expressions
- Randomization with the `random` module
- Input validation and exceptions
- `pytest` and parameterized tests
- Mocking with `unittest.mock.patch`
- Separating application logic from the program entry point

## Future Improvements

- Build an interactive graphical interface using Streamlit.
- Allow users to choose the number of simulations.
- Visualize win rates with charts.
- Let users play individual rounds interactively.

## License

This project is intended for learning and practice.
